import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from drone_msgs.msg import MotorPercs, MotorCmd
from rclpy.qos import QoSPresetProfiles
import pigpio
from time import sleep


class Motor(Node):

    def __init__(self):
        super().__init__('motor_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('pins', [0, 0, 0, 0]),
                ('esc_max', 0),
                ('esc_min', 0),
                ('debug', False)
            ]
        )

        self.pins = self.get_parameter('pins').get_parameter_value().integer_array_value
        self.esc_max = self.get_parameter('esc_max').get_parameter_value().integer_value
        self.esc_min = self.get_parameter('esc_min').get_parameter_value().integer_value
        self.debug = self.get_parameter('debug').get_parameter_value().bool_value

        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()
        
        for pin in self.pins:
            self.pi.set_servo_pulsewidth(pin, 0)
        self.armed = False
        self.throttle = [-1, -1, -1, -1]

        self.create_subscription(MotorCmd, "motor_cmd", self.cmd_callback, QoSPresetProfiles.get_from_short_key('system_default'))
        self.create_subscription(MotorPercs, "motor_vel", self.speed_callback, QoSPresetProfiles.get_from_short_key('sensor_data'))

    def cmd_callback(self, msg: MotorCmd):
        cmd = msg.cmd

        if cmd == MotorCmd.CMD_ARM:
            self.arm()

        elif cmd == MotorCmd.CMD_CALIBRATE:
            self.calibrate()

    def calibrate(self):
        self.get_logger().info("Calibrating...")
        self.set_servos_pulsewidth(0)
        self.get_logger().info("You have 10sec to cisconnect batterty")
        self.countdown(20)

        self.set_servos_pulsewidth(self.esc_max)
        self.get_logger().info("You have 30sec to connect battery and hear confirmation sound")
        self.countdown(20)
        sleep(2)

        self.set_servos_pulsewidth(self.esc_min)
        self.get_logger().info("Calibrating...")
        self.countdown(5)
        self.set_servos_pulsewidth(0)

        self.arm()

    def countdown(self, n):
        for i in range(n):
            self.get_logger().info(str(n-i))
            sleep(1)

    def arm(self):
        self.get_logger().info("Arming...")
        self.set_servos_pulsewidth(0)
        sleep(1)
        self.set_servos_pulsewidth(self.esc_max)
        sleep(1)
        self.set_servos_pulsewidth(self.esc_min)
        sleep(1)
        
        self.armed = True
        self.get_logger().info("Done arming!")

    def set_servos_pulsewidth(self, val: int):
        for n, pin in enumerate(self.pins):
            self.pi.set_servo_pulsewidth(pin, val)
            self.throttle[n] = ((val - self.esc_min) / self.esc_max) if self.esc_min <= val <= self.esc_max else -1

    def speed_callback(self, msg: MotorPercs):
        vel = list(msg.vel)
        # self.get_logger().info("Received speed: {}".format(vel))
        
        dbg = []
        for n, val in enumerate(vel):
            tmp =  min(max(self.esc_min, self.esc_min + val * (self.esc_max - self.esc_min)), self.esc_max)
            self.pi.set_servo_pulsewidth(self.pins[n], tmp)
            dbg.append(tmp)
        
        self.get_logger().info("Set speed: {}".format(dbg))

    def kill(self):
        for pin in self.pins:
            self.pi.write(pin, 0)
        self.pi.stop()

def main(args=None):
    rclpy.init(args=args)
    node = Motor()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()