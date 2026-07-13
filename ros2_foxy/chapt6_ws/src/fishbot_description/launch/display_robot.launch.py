import launch
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the path to the URDF file
    urdf_file_path = get_package_share_directory('fishbot_description')
    urdf_path = os.path.join(urdf_file_path, 'urdf', 'first_robot.urdf')
    rviz_config_path = os.path.join(get_package_share_directory('fishbot_description'), 'config', 'rviz.rviz')

    # 声明一个urdf目录的参数，方便修改
    action_declare_arg_mode_path = launch.actions.DeclareLaunchArgument(
        name='model',
        default_value=urdf_path,
        description='Path to the URDF file'
    )

    # # Create a launch description
    # ld = launch.LaunchDescription()

    # Add the robot_state_publisher node to the launch description
    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_path).read()}]
    )

    action_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
    )

    action_rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path]
    )

    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        action_robot_state_publisher,
        action_joint_state_publisher,
        action_rviz_node,
    ])