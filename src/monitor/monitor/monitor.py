# This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSPresetProfiles
from std_msgs.msg import String
from sensor_msgs.msg import Imu, NavSatFix
from drone_msgs.msg import 
from .ui_window import Ui_MainWindow


class MonitorApp(QMainWindow):

    def __init__(self, ros_args):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start(1)

        rclpy.init(args=ros_args)
        self.executor = MultiThreadedExecutor()
        self.node = Node('monitor')

        self.node.create_subscription(String, 'test', self.callback, QoSPresetProfiles.Profile0)

        self.executor.add_node(self.node)

    def callback(self, msg):
        self.node.get_logger().info("Test: %s" % msg.data)
        print("Test: %s" % msg.data)

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
