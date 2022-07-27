from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('control'),
        'config',
        'params.yaml'
    )

    ld = LaunchDescription()

    ld.add_entity(
        Node(
            package = 'control',
            executable =  'pid',
            name = 'pid_controller',
            # output = {'both': 'log'},
            parameters = [config],
        )
    )

    return ld