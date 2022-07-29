import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from rclpy.qos import QoSPresetProfiles
import pigpio
from time import sleep, time


class Ping(Node):

    def __init__(self):
        super().__init__('buzzer_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('trig_pin', 0),
                ('echo_pin', 0),
                ('freq', 0.0),
                ('debug', False),
            ]
        )

        self.trig_pin = self.get_parameter('trig_pin').get_parameter_value().integer_value
        self.echo_pin = self.get_parameter('echo_pin').get_parameter_value().integer_value
        self.freq = self.get_parameter('freq').get_parameter_value().double_value
        self.debug = self.get_parameter('debug').get_parameter_value().bool_value

        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()

        self.pi.set_mode(self.trig_pin, pigpio.OUTPUT)
        self.pi.set_mode(self.echo_pin, pigpio.INPUT)
        sleep(2)

        self.pub = self.create_publisher(Float32, "ping_height", QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.create_timer(1.0 / self.freq, self.callback)

    def callback(self):
        sleep(0.0001)
        self.pi.write(self.trig_pin, 1)
        sleep(0.00001)
        self.pi.write(self.trig_pin, 0)

        t1 = t2 = None
        t = time()
        while self.pi.read(self.echo_pin) == 0:
            t1 = time()
            if t1 - t > 0.01:
                return
        
        while self.pi.read(self.echo_pin) == 1 and t1 is not None:
            t2 = time()
            if (t2 - t1) * 171.5 > 4:
                t2 = None
                break

        msg = Float32()
        if t1 is None:
            msg.data = 0.0
        elif t2 is None:
            msg.data = -1.0
        else:
            msg.data = (t2 - t1) * 171.5
        # self.get_logger().info(f'{msg.data}')
        self.pub.publish(msg)

    def kill(self):
        self.pi.write(5, 0)
        self.pi.stop()

def main(args=None):
    rclpy.init(args=args)
    node = Ping()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
