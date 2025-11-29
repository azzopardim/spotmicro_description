from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():
    pkg_share = get_package_share_directory('spotmicro_description')
    xacro_path = os.path.join(pkg_share, 'urdf', 'spotmicroai.urdf.xacro')
    robot_description = xacro.process_file(xacro_path).toxml()

    rviz_config = os.path.join(pkg_share, 'rviz', 'view_rviz2.rviz')

    return LaunchDescription([
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            parameters=[{
                'robot_description': robot_description,
                'publish_default_positions': True,
                'rate': 30.0,
                'use_gui': False,
            }],
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            parameters=[{'robot_description': robot_description}],
            output='screen',
        ),
    ])
