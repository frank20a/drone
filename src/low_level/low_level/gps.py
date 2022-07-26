import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix, NavSatStatus
from rclpy.qos import QoSPresetProfiles
from serial import Serial
from pynmeagps import NMEAReader
from pynmeagps.exceptions import *
from time import sleep


class GPS(Node):

    def __init__(self):
        super().__init__('gps_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('baud', 0),
                ('freq', 0),
                ('debug', False),
            ]
        )

        self.baud = self.get_parameter('baud').get_parameter_value().integer_value
        self.freq = self.get_parameter('freq').get_parameter_value().integer_value
        self.debug = self.get_parameter('debug').get_parameter_value().bool_value

        stream = Serial('/dev/ttyS0', self.baud, timeout=3)
        self.nmr = NMEAReader(stream)

        self.pub = self.create_publisher(NavSatFix, 'gps', QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.create_timer(1 / self.freq, self.publish_gps)

    def publish_gps(self):
        try:
            for _, data in self.nmr:
                if data.msgID == 'GGA':
                    msg = NavSatFix()

                    msg.header.stamp = self.get_clock().now().to_msg()
                    msg.header.frame_id = 'gps'

                    msg.status.status = NavSatStatus.STATUS_NO_FIX if data.quality == 0 else NavSatStatus.STATUS_FIX
                    msg.status.service = 15 if data.quality != 0 else 0

                    msg.latitude = float(data.lat if data.lat != '' else 0)
                    msg.longitude = float(data.lon if data.lon != '' else 0)
                    msg.altitude = float(data.alt if data.alt != '' else 0)
                    msg.position_covariance = [
                        float(data.HDOP), 0.0, 0.0,
                        0.0, float(data.HDOP), 0.0,
                        0.0, 0.0, 0.0
                    ]
                    msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_APPROXIMATED
                    
                    self.pub.publish(msg)
        except NMEAParseError:
            pass

    def kill(self):
        self.ser.close()

def main(args=None):
    rclpy.init(args=args)
    node = GPS()
    rclpy.spin(node)

    node.kill()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
