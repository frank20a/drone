import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
from rclpy.qos import QoSPresetProfiles
import pigpio
from time import sleep


class Battery(Node):

    def __init__(self):
        super().__init__('battery_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('debug', False),
            ]
        )

        self.debug = self.get_parameter('debug').get_parameter_value().bool_value

        self.pi = pigpio.pi()
        if not self.pi.connected:
            self.get_logger().error("PI NOT CONNECTED")
            exit()

        self.create_publisher(BatteryState, 'battery', QoSPresetProfiles.get_from_short_key('sensor_data'))

    def kill(self):
        self.pi.write(5, 0)
        pi.stop()

def main(args=None):
    rclpy.init(args=args)
    node = Battery()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()