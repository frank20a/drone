# This Python file uses the following encoding: utf-8
import os
import sys
from this import d
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
from PySide6.QtCore import QDateTime, QTime, QDate
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSPresetProfiles
from std_msgs.msg import Float32
from sensor_msgs.msg import Imu, NavSatFix
from drone_msgs.msg import BuzzerCmd, DateTime, DroneSetpoint4, MotorCmd
from .ui_window import Ui_MainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from ament_index_python import get_package_share_directory
from folium import Map, Circle
import io


class MonitorApp(QMainWindow):

    def __init__(self, ros_args):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open(os.path.join(get_package_share_directory('monitor'), 'config', 'mapbox_public_token.txt')) as f:
            self.token = f.read().strip('\n')

        self.ui.thrust.sliderMoved.connect(self.thrust_callback)
        self.ui.thrust.sliderReleased.connect(self.thrust_reset)

        self.ui.roll.sliderMoved.connect(self.roll_callback)
        self.ui.roll.sliderReleased.connect(self.roll_reset)

        self.ui.pitch.sliderMoved.connect(self.pitch_callback)
        self.ui.pitch.sliderReleased.connect(self.pitch_reset)

        self.ui.yaw.sliderMoved.connect(self.yaw_callback)
        self.ui.yaw.sliderReleased.connect(self.yaw_reset)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start(1)

        rclpy.init(args=ros_args)
        self.executor = MultiThreadedExecutor()
        self.node = Node('monitor')

        self.node.create_subscription(Float32, 'ping_height', self.ping_callback, QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.node.create_subscription(Imu, 'imu', self.imu_callback, QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.node.create_subscription(NavSatFix, 'gps', self.gps_callback, QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.node.create_subscription(DateTime, 'gps_time', self.date_time_callback, QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.motor_cmd_pub = self.node.create_publisher(MotorCmd, 'motor_cmd', QoSPresetProfiles.get_from_short_key('sensor_data'))
        self.drone_setpoint_pub = self.node.create_publisher(DroneSetpoint4, 'drone_setpoint', QoSPresetProfiles.get_from_short_key('sensor_data'))

        self.executor.add_node(self.node)

    def pitch_reset(self):
        self.ui.pitch.setSliderPosition(0)
        self.pitch_callback()

    def pitch_callback(self):
        msg = DroneSetpoint4()
        msg.roll = 0.0
        msg.pitch = self.ui.pitch.value() / 1000
        msg.yaw = 0.0
        msg.alt = 0.0
        self.drone_setpoint_pub.publish(msg)

    def yaw_reset(self):
        self.ui.yaw.setSliderPosition(0)
        self.yaw_callback()

    def yaw_callback(self):
        msg = DroneSetpoint4()
        msg.roll = 0.0
        msg.pitch = 0.0
        msg.yaw = self.ui.yaw.value() / 1000
        msg.alt = 0.0
        self.drone_setpoint_pub.publish(msg)

    def roll_reset(self):
        self.ui.roll.setSliderPosition(0)
        self.roll_callback()

    def roll_callback(self):
        msg = DroneSetpoint4()
        msg.roll = self.ui.roll.value() / 1000
        msg.pitch = 0.0
        msg.yaw = 0.0
        msg.alt = 0.0
        self.drone_setpoint_pub.publish(msg)

    def thrust_reset(self):
        self.ui.thrust.setSliderPosition(0)
        self.thrust_callback()

    def thrust_callback(self):
        msg = DroneSetpoint4()
        msg.roll = 0.0
        msg.pitch = 0.0
        msg.yaw = 0.0
        msg.alt = self.ui.thrust.value() / 1000
        self.drone_setpoint_pub.publish(msg)

    def ping_callback(self, msg: Float32):
        self.ui.ping_height.display(int(msg.data * 100) / 100)

    def imu_callback(self, msg: Imu):
        pass

    def gps_callback(self, msg: NavSatFix):
        if msg.status.status <= 0:
            self.ui.gps_status.setText('NoFix')
        else:
            self.ui.gps_status.setText('Fix')

            m = Map(
                location = [38.0599892, 23.7924013],
                zoom_start = 15,
                tiles = 'Stamen Terrain',
            )

            Circle(
                location=(msg.latitude, msg.longitude),
                radius=100,
                popup="Drone Position",
                colorcolor='crimson',
                fill=True,
            ).add_to(m)

            # self.ui.map.setHtml(m.get_root().render())

    def date_time_callback(self, msg: DateTime):
        self.ui.gps_time.setDateTime(QDateTime(date=QDate(msg.year, msg.month, msg.day), time=QTime(msg.hour, msg.minute, msg.second)))

    def __del__(self):
        self.node.destroy_node()
        rclpy.shutdown()

    def timer_update(self):
        self.show()
        rclpy.spin_once(self.node, executor=self.executor, timeout_sec=0.01)
        self.timer.start(1)

def main(args=None):
    app = QApplication(sys.argv)

    win = MonitorApp(args)
    win.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
