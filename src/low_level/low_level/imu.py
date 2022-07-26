import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from rclpy.qos import QoSPresetProfiles
from time import sleep

import sys, os, RTIMU
from ament_index_python import get_package_share_directory
from tf_transformations import quaternion_from_euler
from time import sleep


settingsfile = os.path.join(
    get_package_share_directory('low_level'),
    'config',
    'RTIMU',
)
s = RTIMU.Settings(settingsfile)
imu = RTIMU.RTIMU(s)
if not imu.IMUInit():
    print('IMU Init Failed')
    sys.exit(1)
else:
    print(f'IMU {imu.IMUName()} initialised')

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()


class IMU(Node):

    def __init__(self):
        global imu, poll_interval

        super().__init__('imu_controller')
        self.declare_parameters(
            namespace = '',
            parameters = [
                ('freq', 0),
                ('debug', False),
            ]
        )

        self.freq = self.get_parameter('freq').get_parameter_value().integer_value
        self.debug = self.get_parameter('debug').get_parameter_value().bool_value

        self.pub = self.create_publisher(Imu, 'imu', QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.create_timer(1.0/self.freq, self.publish_imu)

    def publish_imu(self):
        global imu, poll_interval

        if imu.IMURead():
            # self.get_logger().info('IMU data read')
            data = imu.getIMUData()

            imu_msg = Imu()

            imu_msg.header.stamp = self.get_clock().now().to_msg()
            imu_msg.header.frame_id = 'imu'

            imu_msg.orientation.x = data['fusionQPose'][0]
            imu_msg.orientation.y = data['fusionQPose'][1]
            imu_msg.orientation.z = data['fusionQPose'][2]
            imu_msg.orientation.w = data['fusionQPose'][3]

            imu_msg.linear_acceleration.x = data['accel'][0]
            imu_msg.linear_acceleration.y = data['accel'][1]
            imu_msg.linear_acceleration.z = data['accel'][2]

            imu_msg.angular_velocity.x = data['gyro'][0]
            imu_msg.angular_velocity.y = data['gyro'][1]
            imu_msg.angular_velocity.z = data['gyro'][2]

            self.pub.publish(imu_msg)
        # else:
        #     self.get_logger().info('No IMU data')


def main(args=None):
    rclpy.init(args=args)
    node = IMU()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
