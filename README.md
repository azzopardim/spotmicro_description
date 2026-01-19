# spotmicro_description

URDF/xacro, meshes, and RViz helpers for the Spot/Nova model. Based on the SpotMicroAI description, with paths adjusted for this package name.

## Usage (ROS 2)
After building the workspace and sourcing setup, you can visualize the model:

```bash
# Launch RViz with the robot description
ros2 launch spotmicro_description view_model.launch.py

# Minimal URDF view (xacro → robot_state_publisher + joint_state_publisher)
ros2 launch spotmicro_description view_urdf_rviz.launch.py
```

To regenerate the URDF from xacro manually:

```bash
ros2 run xacro xacro $(ros2 pkg prefix spotmicro_description)/share/spotmicro_description/urdf/spotmicroai.urdf.xacro > /tmp/spotmicroai.urdf
```
