import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from drone_msgs.msg import DroneSetpoint4, MotorPercs, ControlFlags4, MotorCmd
from rclpy.qos import QoSPresetProfiles
import pigpio
from simple_pid import PID
import numpy as np
from tf_transformations import euler_from_quaternion
from .mma import MMA


class PIDController(Node):

    def __init__(self):
        super().__init__('pid_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('freq', 0.0),
                ('tune_r', [0.0, 0.0, 0.0]),
                ('tune_p', [0.0, 0.0, 0.0]),
                ('tune_y', [0.0, 0.0, 0.0]),
                ('tune_t', [0.0, 0.0, 0.0]),
                ('debug', False),
            ]
        )

        rp, ri, rd = list(self.get_parameter('tune_r').get_parameter_value().double_array_value)
        pp, pi, pd = list(self.get_parameter('tune_p').get_parameter_value().double_array_value)
        yp, yi, yd = list(self.get_parameter('tune_y').get_parameter_value().double_array_value)
        tp, ti, td = list(self.get_parameter('tune_t').get_parameter_value().double_array_value)
        self.freq = self.get_parameter('freq').get_parameter_value().double_value
        self.debug = self.get_parameter('debug').get_parameter_value().bool_value
        
        rp, ri, rd = 2.0, 0.01, 0.5
        pp, pi, pd = 2.0, 0.01, 0.5
        yp, yi, yd = 2.0, 0.01, 0.5
        tp, ti, td = 0.0, 0.0, 0.0

        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()
        
        # Roll, Pitch, Yaw, Thrust
        self.pids = (
            PID(rp, ri, rd),
            PID(pp, pi, pd),
            PID(yp, yi, yd),
            PID(tp, ti, td),
        )
        for pid in self.pids:
            pid.sample_time = 1.0 / self.freq
            # pid.output_limits = (0.0, 1.0)

        self.state = np.array([
            np.NaN,
            np.NaN,
            np.NaN,
            np.NaN,
            np.NaN,
            np.NaN,
        ])

        self.setpoint = np.array([
            0.0,
            0.0,
            0.0,
            0.0
        ])

        self.control_flags = [
            True,
            True,
            False,
            False
        ]

        self.control = np.array([
            0.0,
            0.0,
            0.0,
            0.0
        ])

        self.create_subscription(Imu, 'imu', self.set_imu, QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.create_subscription(DroneSetpoint4, 'setpoint', self.get_setpoint, QoSPresetProfiles.get_from_short_key('system_default'))
        self.create_subscription(DroneSetpoint4, 'control', self.get_control, QoSPresetProfiles.get_from_short_key('system_default'))
        self.create_subscription(ControlFlags4, 'control_flags', self.get_flags, QoSPresetProfiles.get_from_short_key('system_default'))
        self.pub = self.create_publisher(MotorPercs, 'motor_vel', QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.create_timer(1.0 / self.freq, self.callback)

        self.arm_pub = self.create_publisher(MotorCmd, 'motor_cmd', QoSPresetProfiles.get_from_short_key('system_default'))
        tmp = MotorCmd()
        tmp.cmd = MotorCmd.CMD_ARM
        self.arm_pub.publish(tmp)

    def callback(self):

        if any(map(np.isnan, self.state[:3])):
            return

        con = []
        for n, pid in enumerate(self.pids):
            if self.control_flags[n]:
                con.append(pid(self.state[n] - self.control[n]))
            else:
                con.append(0.0)
        con = MMA(con)

        # self.get_logger().info(f'{con}')
        # self.get_logger().info(f'{self.state[:3]}')

        msg = MotorPercs()
        msg.vel = con
        self.pub.publish(msg)

    def get_flags(self, msg: ControlFlags4):
        for n, i in enumerate(list(msg.flags)):
            self.control_flags[n] = bool(i)

    def get_setpoint(self, msg: DroneSetpoint4):
        self.setpoint[0] = msg.roll
        self.setpoint[1] = msg.pitch
        self.setpoint[2] = msg.yaw
        self.setpoint[3] = msg.alt

    def get_control(self, msg: DroneSetpoint4):
        self.control[0] = msg.roll
        self.control[1] = msg.pitch
        self.control[2] = msg.yaw
        self.control[3] = msg.alt

    def set_imu(self, msg: Imu):
        euler = euler_from_quaternion((msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w))

        self.state[0:3] = euler

    def kill(self):
        pass

def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
