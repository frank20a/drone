from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
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

    ld.add_entity(
        Node(
            package = 'low_level',
            executable =  'imu',
            name = 'imu_controller',
            # output = {'both': 'log'},
            parameters = [config],
        )
    )

    ld.add_entity(
        Node(
            package = 'low_level',
            executable =  'gps',
            name = 'gps_controller',
            # output = {'both': 'log'},
            parameters = [config],
        )
    )

    # ld.add_entity(
    #     Node(
    #         package = 'low_level',
    #         executable =  'battery',
    #         name = 'battery_controller',
    #         # output = {'both': 'log'},
    #         parameters = [config],
    #     )
    # )
    
    # ld.add_entity(
    #     Node(
    #         package = 'low_level',
    #         executable =  'ping',
    #         name = 'ping_controller',
    #         # output = {'both': 'log'},
    #         parameters = [config],
    #     )
    # )

    return ld