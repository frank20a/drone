import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from rclpy.qos import QoSPresetProfiles
import pigpio
from time import sleep


class GPS(Node):

    def __init__(self):
        super().__init__('gps_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('pin', 0),
                ('debug', False),
            ]
        )

        self.pin = self.get_parameter('pin').get_parameter_value().integer_value
        self.debug = self.get_parameter('debug').get_parameter_value().boolean_value

        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()

        self.create_publisher(NavSatFix, 'gps', QoSPresetProfiles.get_from_short_key('sensor_data'))

    def kill(self):
        self.pi.write(5, 0)
        pi.stop()

def main(args=None):
    rclpy.init(args=args)
    node = GPS()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()