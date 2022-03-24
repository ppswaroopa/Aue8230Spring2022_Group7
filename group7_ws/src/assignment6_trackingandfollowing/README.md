## Homework 6 submission

Package Name: assignment6_trackingandfollowing
ROS Version: Noetic
Required Package: 
	1. gazebo
	2. apriltag (AprilTag3)
	3. apriltag_ros (3.1.2)

Prerequesite:
 - Clone https://github.com/AprilRobotics/apriltag and https://github.com/AprilRobotics/apriltag_ros into your workspace.
 - Run in your workspace
 ```
 - $ cmake_isolated
 ```
 - To use the the routine that uses apriltag package, make sure to run both of these:
 ```
 $ source devel/setup.bash
 $ source devel_isolated/setup.bash
 ```
This package contains one routine performed on the Turtlebot3 Burger in Gazebo Simulation and two routines implemented to perform in the real turtlebot3 burger.

### How to Run
Clone package folder into the catkin_workspace/src
```
$ catkin_make
$ roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch # Replace the launch file name with any other
```
### Demo
1. wall_follower.py: Run the turtlebot in Gazebo with constant forward velocity while maintaining equal distances from the wall. A PD controller is implemented to keep the robot at the center between the walls.
![](/screenshot/wall_follower.png)
2. wander.py: Run the turtlebot in Gazebo around the world provided while avoiding any obstacle
![](/screenshot/wander.png)
3. obstacle_avoidance_realworld.py: This routine is run with the real robot. This is an implementation of the wander.py adapted to run in the real world obstacles.
![](/screenshot/real_world.png)

### Demo Videos
Videos folder inside the package contains demo runs of all the scripts.
