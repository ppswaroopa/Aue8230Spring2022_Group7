#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def square_openloop():
    rospy.init_node("square_openloop", anonymous=True)
    rospy.loginfo("Turtlebot started running in square (open-loop control)")
    vel_pub=rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    
    lin_vel=Twist()
    lin_vel.linear.x = 0.3
    ang_vel=Twist()
    ang_vel.angular.z = 0.3

    lin = 1
    st=time.time()

    while not rospy.is_shutdown():
        if lin==1:        
            vel_pub.publish(lin_vel)
            time.sleep(1.1)
            if time.time()-st>=5:                
                lin=0
                st=time.time()
        if lin==0:
            vel_pub.publish(ang_vel)
            time.sleep(1.1)
            if time.time()-st>=5.7:
                lin=1
                st=time.time()

if __name__=="__main__":
    try:
        square_openloop()
    except rospy.ROSInterruptException:
        pass