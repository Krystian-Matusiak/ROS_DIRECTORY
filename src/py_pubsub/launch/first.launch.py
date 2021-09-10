import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'py_pubsub',
            default_value=[launch.substitutions.EnvironmentVariable('USER'), '_'],
            description='py_pubsub'),
        launch_ros.actions.Node(
            package='demo_nodes_cpp', executable='talker', output='screen',
            name=[launch.substitutions.LaunchConfiguration('py_pubsub'), 'talker']),
    ])
