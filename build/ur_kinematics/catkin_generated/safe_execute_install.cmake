execute_process(COMMAND "/home/bonato/Documents/ridgeback_ur5/build/ur_kinematics/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/bonato/Documents/ridgeback_ur5/build/ur_kinematics/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
