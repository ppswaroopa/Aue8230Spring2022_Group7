## Homework 6 submission

Package Name: assignment6_trackingandfollowing<br>
ROS Version: Noetic<br>
Required Packages: <br>
	1. gazebo<br>
	2. apriltag (AprilTag3)<br>
	3. apriltag_ros (3.1.2)<br>

Prerequisite:
 - Clone https://github.com/AprilRobotics/apriltag and https://github.com/AprilRobotics/apriltag_ros into your workspace.
 ```
 $ cd ~/catkin_workspace/
 $ cmake_isolated
 ```
 - To use the the routine that uses apriltag package, always include the setup.bash from devel_isolated together with the standard one:
 ```
 $ source devel/setup.bash
 $ source devel_isolated/setup.bash
 ```
This package contains one routine performed on the Turtlebot3 Burger in Gazebo Simulation and two routines implemented to perform in the Real life.

### How to Run
Clone package folder into the catkin_workspace/src
```
$ catkin_make
$ roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch # Replace the launch file name with any other
```
### Demo
1. follow_line_step_hsv.py: Run the turtlebot in Gazebo with constant forward velocity while following the line in the 'follow_line.world' file. A PD controller is implemented to follow the lane.
![](/screenshot/turtlebot3_follow_line_map.png)
2. follow_line_step_hsv_real.py: To run the 1st routine in the Real world
![](/screenshot/turtlebot3_follow_line_realworld.png)
3. april_tag.py: Tracking an april tag of family 'Tag36h11' id:0 and maintains a constant distance of 0.3m. Make sure to follow the 'Prerequisite' and also replace the files found in 'catkin_workspace/src/apriltag_ros/apriltag_ros/config' with the ones provided in the 'other_res' directory<br>
![Screen Record](/screenshot/apriltag_ros.png)
!["Real World"](/screenshot/apriltag_ros_real.png)

### Demo Videos
Videos folder inside the package contains demo runs of all the scripts in simulation and real world.

