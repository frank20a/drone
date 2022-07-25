from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription, ExecuteProcess
import os

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('low_level'),
        'config',
        'params.yaml'
    )

    ld = LaunchDescription()

    ld.add_entity(
        Node(
            package = 'low_level',
            executable =  'buzzer',
            name = 'buzzer_controller',
            # output = {'both': 'log'},
            parameters = [config],
        )
    )

    ld.add_entity(
        Node(
            package = 'low_level',
            executable =  'motor',
            name = 'motor_controller',
            # output = {'both': 'log'},
            parameters = [config],
        )
    )
    
    return ld