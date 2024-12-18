ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}

SHELL ["/bin/bash", "-c"]

### Add a few tools
RUN sudo apt update && sudo apt install -y \
    bash-completion \
    silversearcher-ag \
    apt-transport-https \
    less \
    alsa-utils \
    ros-rolling-ur \
    ros-${ROS_DISTRO}-ur-msgs \
    ros-${ROS_DISTRO}-ur-robot-driver \
    && sudo apt upgrade -y && sudo apt clean
### apt update and clean
RUN sudo apt update && sudo apt upgrade -y && sudo apt clean




WORKDIR /home/
RUN git clone --depth 1 https://github.com/epfl-lasa/ur5_lasa.git

RUN cp -R ur5_lasa/docker_interface_ros2/src/ ros_ws/src/

# Cleaning the workspace
RUN rm -r /home/ur5_lasa

### Build ros workspace
WORKDIR /home/ros_ws
RUN rosdep update
RUN source /home/ros_ws/ .bashrc && rosdep install --from-paths src --ignore-src -r -y


# RUN ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur5 robot_ip:=127.0.0.1
#-------------------------------------------------------------------------------
RUN echo "cd /home/ros_ws" >> ~/.bashrc
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
# RUN echo "catkin build" >> ~/.bashrc
# RUN echo "source install/setup.bash" >> ~/.bashrc
# RUN echo "roslaunch wp5_tasks integrationShotcreteKUL.launch" >> ~/.bashrc