# Set the ROS distribution dynamically
ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}

# Use bash shell for all subsequent commands
SHELL ["/bin/bash", "-c"]

RUN apt update && apt-get install -y curl gnupg2 lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - && \
    echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros2-latest.list


# Update and install essential tools\  and ROS packages
RUN apt update --fix-missing && \ 
    apt install -y --no-install-recommends \    
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
WORKDIR /home/ros2_ws/src 
COPY src/ .
WORKDIR /home/ros2_ws/

# Set up ROS environment and install dependencies using rosdep
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    sudo rosdep fix-permissions && \
    rosdep update && \
    rosdep install --from-paths src --ignore-src -r -y

# Build the ROS workspace using colcon
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    colcon build

# Add ROS environment sourcing to the bashrc for interactive sessions
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc && \
    echo "source /home/ros2_ws/install/setup.bash" >> ~/.bashrc 
    # && \
    # echo "ros2 launch ur_robot_driver ur_control.launch.py ur_type:=ur5 robot_ip:=127.0.01" >> ~/.bashrc

# Default command to run bash shell with ROS environment setup
CMD ["bash"]
