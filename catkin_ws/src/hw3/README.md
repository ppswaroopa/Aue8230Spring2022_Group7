# Task 1-1:
The launch file has been created with the name circle.launch.
This launch file contains commands to first launch the gazebo with turtlebot3_empty_world environment with turtlebot3 in it.
Once the gazebo is launched, the node circle.py is started to move the turtlebot3 in a circular path.

Command to launch: roslaunch hw3 circle.launch



# Task 1-2:
The launch file has been created with the name square.launch.
This launch file contains commands to first launch the gazebo with turtlebot3_empty_world environment with turtlebot3 in it.
Once the gazebo is launched, the node square.py is started to move the turtlebot3 in a square path.

Command to launch: roslaunch hw3 square.launch



# Task 1-3:
The launch file has been created with the name move.launch.
This launch file contains commands to first launch the gazebo with turtlebot3_empty_world environment with turtlebot3 in it.
Once the gazebo is launched, based on the user input for code argument (circle or square), the node circle.py or square.py is started to move the turtlebot3 in a circular or square path.

Command to launch: roslaunch hw3 move.launch code:=(circle or square)



# Task 2-1:
The launch file has been created with the name line.launch.
This launch file contains commands to first launch the gazebo with turtlebot3_wall_world environment with wall present infront of turtlebot3 at some distance in it.
Once the gazebo is launched, the node line.py is started to move the turtlebot3 in a linear path towards the wall.
As soon as the distance between wall and turtlebot3 becomes less than 0.5, the turtlebot3 stops.

Command to launch: roslaunch hw3 line.launch





