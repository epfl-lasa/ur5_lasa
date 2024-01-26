# UR5 on Ridgeback Platform

This repository is a comprehensive guide for utilizing the Universal Robots UR5 robotic arm mounted on the Ridgeback mobile base platform.

Purpose:
The purpose of this repository is to provide detailed instructions and resources on using the UR5 robot arm in conjunction with the Ridgeback mobile base. It covers three primary aspects:

## 1) Setup and Requirements for UR5 on Ridgeback
- All the packages provided in the 'src' folder are necessary to control the UR5 with ROS. These packages are modified versions derived from the Universal Robot repository (https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git). The main modifications include the addition of some ROS controllers, configuration of files specific to our real UR5, and simplification of the 'roslaunch' command to easily select various types of controllers. This setup also serves as an example for adding additional controllers if desired.

- you need to have the ros control package : sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers

## 2) Real Robot Usage on Ridgeback
To effectively control the UR5 using ROS, the integration requires the use of the Polyscope interface connected to the robot (image) and the preconfigured 'roslaunch' provided by Universal Robots. This integration is facilitated through URCAPS, already set up on the robot for seamless usage with ROS.


### Startup:
a) Power on both the Ridgeback and the UR5.

### Polyscope Setup:
a) On the Polyscope interface, navigate to:
    - 'Run Program'
    - Load the 'urcap_ros' file (Polyscope Image)
All necessary configurations are preloaded.

### Launching Controllers:
a) Launch the preferred controller on the inboard computer using provided commands.
 Each predefined launch incorporates the named controller and loads the position joint controller within. Custom launch files can later be created to include additional controllers.
 For example: roslaunch ur_lasa ur5_bringup_vel_controller.launch 

### Activating Control:
a) Initiate control by pressing 'Play' on the Polyscope interface (Polyscope image).

Once these steps are completed, publish commands to desired topics. For instance, for the twist controller:
/ur5/twist_controller/command Ensure using the appropriate message type for command publication.

<img width="598" alt="polyscope" src="https://github.com/bonato47/ridgeback_ur5/assets/61695400/6602d7c3-0cf7-450e-83ef-2ee70f2d69eb">


All controllers defined in 'ur5_lasa/config/ur5_controllers' are accessible. Utilize ROS services to load and switch between controllers.
example:
- see the loaded controllers: 
rosservice call /ur5/controller_manager/list_controllers   
- switch controllers twist to pos: 
rosservice call /ur5/controller_manager/switch_controller "start_controllers: ['joint_group_pos_controller']
stop_controllers: ['twist_controller']
strictness: 2
start_asap: false
timeout: 0.0" 


## 3) Simulation Usage for UR5 on Ridgeback
The simulation is using the same tools as the real robot; the polyscope and the ur_robot_driver.
To have a simualted polyscope you need to build and start the docker_polyscope. 
It will open a GUI exaccly replicating the real polyscope. Everything is preconfigured on the docker as well. 
you just need to create a bridge with the docker and the virtual robot with these commands:
docker network create --subnet=192.168.56.0/24 ursim_net
docker run --rm -it --net ursim_net --ip 192.168.56.101 -d universalrobots/ursim_cb3


You juste need to do it as it was a real robot plus launch rviz : 
roslaunch ur_lasa ridgeback_rviz.launch

Furthemore, if later you want to create different programs, it has a volume bind to the docker. So you can save all the programs you want.







