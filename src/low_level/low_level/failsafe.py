import rclpy
from rclpy.node import Node
from std_msgs.msg import Empty
from rclpy.qos import QoSPresetProfiles
import pigpio
from time import sleep


class Failsafe(Node):

    def __init__(self):
        super().__init__('failsafe')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('pins', [0, 0, 0, 0]),
                ('esc_min', 0),
            ]
        )

        self.pins = self.get_parameter('pins').get_parameter_value().integer_array_value
        self.esc_min = self.get_parameter('esc_min').get_parameter_value().integer_value
        
        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()

        self.flag = True
        self.counter = 0

        self.create_subscription(Empty, "reset_failsafe", self.callback, QoSPresetProfiles.get_from_short_key('system_default'))
        self.create_timer(1.5, self.reset)

    def reset(self):
        if not self.flag:
            if self.counter < 2:
                self.set_servos_pulsewidth(self.esc_min)
            self.counter += 1
            return

        self.counter = 0
        self.flag = False

    def set_servos_pulsewidth(self, val: int):
        for n, pin in enumerate(self.pins):
            self.pi.set_servo_pulsewidth(pin, val)
            # self.throttle[n] = ((val - self.esc_min) / self.esc_max) if self.esc_min <= val <= self.esc_max else -1

        self.get_logger().error(">> F A I L S A F E <<")

    def callback(self, msg: Empty):
        self.flag = True

    def kill(self):
        for pin in self.pins:
            self.pi.write(pin, 0)
        self.pi.stop()

def main(args=None):
    rclpy.init(args=args)
    node = Failsafe()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()