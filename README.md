UR5 on Ridgeback Platform
This repository is a comprehensive guide for utilizing the Universal Robots UR5 robotic arm mounted on the Ridgeback mobile base platform.

Purpose:
The purpose of this repository is to provide detailed instructions and resources on using the UR5 robot arm in conjunction with the Ridgeback mobile base. It covers three primary aspects:

1) Setup and Requirements for UR5 on Ridgeback
- All the packages provided in the 'src' folder are necessary to control the UR5 with ROS. These packages are modified versions derived from the Universal Robot repository (link). The main modifications include the addition of ROS controllers, configuration of files specific to our real UR5, and simplification of the 'roslaunch' command to easily select various types of controllers. This setup also serves as an example for adding additional controllers if desired.

2) Real Robot Usage on Ridgeback
To effectively control the UR5 using ROS, the integration requires the use of the Polyscope interface connected to the robot (image) and the preconfigured 'roslaunch' provided by Universal Robots. This integration is facilitated through URCAPS, already set up on the robot for seamless usage with ROS.

Follow these steps:

Startup:
a) Power on both the Ridgeback and the UR5.

Polyscope Setup:
a) On the Polyscope interface, navigate to:
    - 'Run Program'
    - Load the 'URCAP_ROS' file (image)
All necessary configurations are preloaded.

Launching Controllers:
a) Launch the preferred controller on the inboard computer using provided commands. For example:
roslaunch ur_robot bringup_twist_controller.launch (Each predefined launch incorporates the named controller and loads the position joint controller within. Custom launch files can later be created to include additional controllers.)

Activating Control:
a) Initiate control by pressing 'Play' on the Polyscope interface (image).

Once these steps are completed, publish commands to desired topics. For instance, for the twist controller:
twist_controller/command Ensure using the appropriate message type for command publication.

All controllers defined in 'config/controller_ur5' are accessible. Utilize ROS services to load and switch between controllers.
example:
- see the loaded controllers: rosservice call /controller_manager/list_controllers   
- switch controllers twist to pos: rosservice call /controller_manager/switch_Controller stop...   

3) Simulation Usage for UR5 on Ridgeback
The simulation is using the same tools as the real robot; the polyscope and the ur_robot_driver.
To have a simualted polyscope you need to build and start the docker_polyscope. 
It will open a GUI exaccly replicating the real polyscope. Everything is preconfigured on the docker as well. 
You juste need to do it as it was a real robot plus launch rviz : 

roslaunch ur_driver rviz_ridgeback.launch







