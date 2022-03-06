## Homework 5 submission

Package Name: hw5_group7
ROS Version: Noetic
Required Package: Gazebo

This package contains 4 different routines performed on the Turtlebot3 Burger in Gazebo Simulation.

### How to Run
Clone package folder into the catkin_workspace/src
$ catkin_make
$ roslaunch hw5_group7 circle.launch # Replace the launch file name with any other

### Demo
All programs run in the Gazebo Simulation Environment
1. circle.py: Run the turtlebot in a circle
![](/screenshot/hw3_circle.png)
2. square.py: Run the turtlebot in 2x2 square with linear velocity = 0.3 and angular velocity = 0.3 
![](/screenshot/hw3_square.png)
3. move.launch: Requires use input in lanch for argument 'code' that will then pick any of the above scripts to run.
  $ roslaunch assignment3_turtlebot3 move.launch code:=square
4. emergency_stop.py: Turtlebot performs an 'emergency breaking' maneuver when detected an obstacle in its path using LIDAR scan.
![](/screenshot/hw3_emergency_stop.png)

### Demo Videos
Videos folder inside the package contains demo runs of all three scripts.
