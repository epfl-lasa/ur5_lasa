#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/bonato/Documents/ridgeback_ur5/src/ur_kinematics"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/bonato/Documents/ridgeback_ur5/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/bonato/Documents/ridgeback_ur5/install/lib/python3/dist-packages:/home/bonato/Documents/ridgeback_ur5/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/bonato/Documents/ridgeback_ur5/build" \
    "/usr/bin/python3" \
    "/home/bonato/Documents/ridgeback_ur5/src/ur_kinematics/setup.py" \
     \
    build --build-base "/home/bonato/Documents/ridgeback_ur5/build/ur_kinematics" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/bonato/Documents/ridgeback_ur5/install" --install-scripts="/home/bonato/Documents/ridgeback_ur5/install/bin"
