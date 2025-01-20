# Set the ROS distribution dynamically
ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}

# Use bash shell for all subsequent commands
SHELL ["/bin/bash", "-c"]

# Update and install essential tools and ROS packages
RUN apt update && apt install -y \
    bash-completion \
    silversearcher-ag \
    apt-transport-https \
    less \
    alsa-utils \
    ros-${ROS_DISTRO}-ur-msgs \
    ros-${ROS_DISTRO}-ur-robot-driver \
    ros-${ROS_DISTRO}-ament-cmake \
    && apt upgrade -y && apt clean

# Set the working directory to the ROS workspace
WORKDIR /home/ros2_ws

# Copy your ROS package into the container
COPY src/Universal_Robots_ROS2_Driver/ src/

# Set up ROS environment and install dependencies using rosdep
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y

# Build the ROS workspace using colcon
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    colcon build

# Add ROS environment sourcing to the bashrc for interactive sessions
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc && \
    echo "source /home/ros2_ws/install/setup.bash" >> ~/.bashrc && \
    echo "ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur5 robot_ip:=127.0.01" >> ~/.bashrc

# Default command to run bash shell with ROS environment setup
CMD ["bash"]
