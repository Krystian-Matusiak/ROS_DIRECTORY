
# Preparation

At first there is a need to install ros2 (better that ros1). When this readme was written latest version was rolling ridley. In this url you can follow the more detailed instructions (package installing etc).

https://docs.ros.org/en/rolling/Installation.html

# Guide

This guide shows how to build and run different ros nodes. At first there is a need to source the setup accordingly to used shell (in my case it is zsh). It has to be in the workspace directory. To test each node you have better source setup for several shells.

```
source install/local_setup.zsh
```

Then there is a need to build all nodes. In case of ROS2 colcon build tool is used:

```
colcon build
```

In first shell you can run example node that simulates GUI:

```
ros2 run py_pubsub gui
```

Then you can run example node for PID in second shell:
```
ros2 run py_pubsub pid
```

In third shell you can run example node that simulates nemo CAN that will publish data to other nodes:
```
ros2 run py_pubsub nemo
```

py_pubsub is example package that has to be installed.

# Future posibilities

There is something liek roslaunch that enables to launch multiple nodes. The only thing that has to be done is to configure XML file.

Each node can be contained in package. We can distinguish main application package (GUI, PID etc), test package (mocked data that simulates e.g. nemo data or camera video stream) and real_robot package (real camera nodes, CAN_nemo). 
