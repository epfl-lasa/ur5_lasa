import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import PythonExpression  # Import PythonExpression for logical evaluation

def determine_robot_ip(context):
    simu_value = context.launch_configurations.get("simu", "OFF")
    return "127.0.0.1" if simu_value.upper() == "ON" else "192.168.131.17"

def generate_launch_description():
    # Declare arguments
    simu_arg = DeclareLaunchArgument("simu", default_value="OFF", description="Set to ON for simulation mode")
    robot_ip_arg = DeclareLaunchArgument("robot_ip", default_value="", description="Robot IP address")
    ft_sensor_arg = DeclareLaunchArgument("ft_sensor", default_value="OFF", description="Set to ON to enable FT sensor")

    # Dynamically set robot IP
    set_robot_ip = OpaqueFunction(function=lambda context: [
        SetLaunchConfiguration("robot_ip", determine_robot_ip(context))
    ])

    # UR Driver Launch
    ur_control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                FindPackageShare('ur_robot_driver').find('ur_robot_driver'),
                'launch',
                'ur_control.launch.py'
            )
        ]),
        launch_arguments={
            "ur_type": "ur5",
            "robot_ip": LaunchConfiguration("robot_ip")
        }.items()
    )

    # FT Sensor Launch (ONLY if ft_sensor=ON)
    ft_sensor_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                FindPackageShare('robotiq_ft_sensor_hardware').find('robotiq_ft_sensor_hardware'),
                'launch',
                'ft_sensor_standalone.launch.py'
            )
        ]),
        condition=IfCondition(PythonExpression(["'", LaunchConfiguration("ft_sensor"), "' == 'ON'"]))
    )

    return LaunchDescription([
        simu_arg,
        robot_ip_arg,
        ft_sensor_arg,
        set_robot_ip,
        ur_control_launch,
        ft_sensor_launch
    ])
