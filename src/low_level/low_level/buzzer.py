import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSPresetProfiles
import pigpio
from time import sleep


class Buzzer(Node):

    def __init__(self):
        super().__init__('buzzer_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('buzzer_pin', 0),
                ('debug', False),
            ]
        )

        self.pin = self.get_parameter('buzzer_pin').get_parameter_value().integer_value
        self.debug = self.get_parameter('debug').get_parameter_value().boolean_value

        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()

        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.create_subscription(String, "buzzer_cmd", self.callback, QoSPresetProfiles.get_from_short_key('system_default'))

    def callback(self, msg: String):
        cmd = msg.data

        if cmd == 'once':
            self.pi.write(self.pin, 1)
            sleep(0.25)
            self.pi.write(self.pin, 0)

        elif cmd == 'on':
            self.pi.write(self.pin, 1)

        elif cmd == 'off':
            self.pi.write(self.pin, 0)

        elif cmd == 'long':
            self.pi.write(self.pin, 1)
            sleep(1)
            self.pi.write(self.pin, 0)

        elif cmd == 'twice':
            self.pi.write(self.pin, 1)
            sleep(0.25)
            self.pi.write(self.pin, 0)
            sleep(0.25)
            self.pi.write(self.pin, 1)
            sleep(0.25)
            self.pi.write(self.pin, 0)
        
        elif cmd == 'error':
            for i in range(40):
                self.pi.write(self.pin, 1)
                sleep(0.5 / 40)
                self.pi.write(self.pin, 0)
                sleep(0.5 / 40)

    def kill(self):
        self.pi.write(5, 0)
        pi.stop()

def main(args=None):
    rclpy.init(args=args)
    node = Buzzer()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()