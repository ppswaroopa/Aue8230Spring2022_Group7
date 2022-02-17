#! /usr/bin/env python3

import rospy
import threading
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def update_scan(scan_data):
    global dist

    dist = min(scan_data.ranges)

def run_scan():
    while not rospy.is_shutdown():
        rospy.Subscriber("/scan", LaserScan, update_scan)
        time.sleep(0.1)

def move():
    global dist

    rospy.init_node("Turtlebot3_line", anonymous=True)
    rospy.loginfo("Turtlebot3 started running towards obstacle")
    vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    vel = Twist()
    time.sleep(2)
    while not rospy.is_shutdown():
        if dist>0.5:
            vel.linear.x = 0.3
            vel_pub.publish(vel)
            time.sleep(1)
        else:
            vel.linear.x = 0
            vel_pub.publish(vel)
            time.sleep(1)
            rospy.loginfo("Obstacle detected, turtlebot stopped")
            break

if __name__=="__main__":
    try:
        dist = 0
        a=threading.Thread(target=run_scan)
        a.start()
        move()
    except rospy.ROSInterruptException:
        a.join()
        pass

