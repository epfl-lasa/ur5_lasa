#!/bin/bash

# Terminal 1: Run the first command in /docker1
gnome-terminal -- bash -c 'cd docker_polyscope && ./start_docker.sh ; exec bash'
gnome-terminal -- bash -c 'cd docker_interface_ros && ./start_docker.sh; exec bash'


