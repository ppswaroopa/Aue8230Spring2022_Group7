## Homework 7 submission

Package Name: assignment7<br>
ROS Version: Noetic<br>
Required Packages: <br>
	1. gazebo<br>
	2. turtlebot3_slam<br>

This package contains one routine performed on the Turtlebot3 Burger in Gazebo Simulation and two routines implemented to perform in the Real life.

### How to Run
Clone package folder into the catkin_workspace/src
```
$ catkin_make
$ roslaunch assignment7 gazebo_slam_LDS.launch # Replace the launch file name with any other
```
### Standard Routine to be followed when running on realbot
Create SSH terminal into the turtlebot. Run the following<br>
```
$ roslaunch turtlebot3_bringup turtlebot3_robot.launch
```
In Remote PC
1. Running Slam Node: https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node <br>
2. Running Navigation Node after mapping: https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#run-navigation-nodes <br>
3. Similiar instructions are available in these links for karto slam.

### Code
1. gazebo_slam_LDS.launch: To use the LDS Lidar of turtlebot to perform GMAP-SLAM algorithm.
![](screenshot/turtlebot3_follow_line_map.png)
2. gazebo_slam_LDS_navigate.launch: To perform navigation based on the map saved by the 1st routine.
![Screen Record](screenshot/turtlebot3_follow_line_realworld_screenrecord.png)
!["Real World"](screenshot/turtlebot3_follow_line_realworld.png)
3. real_gmap_LDS_navigate.launch & real_karto_LDS_slam_navigate.launch: These routines are to launch navigation nodes for running in the real world.<br>
![Screen Record](screenshot/apriltag_ros.png)
!["Real World"](screenshot/apriltag_ros_real.png)

### Demo Videos
Videos folder inside the package contains demo runs of all the scripts in simulation and real world.
