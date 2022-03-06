#!/usr/bin/env python3

from audioop import lin2adpcm
from re import L
from tkinter import E
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import pi, sqrt

class TurtleBot:
    def __init__(self):

        rospy.init_node('square_openloop', anonymous=True)

        self.velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
        self.lidar_sub = rospy.Subscriber('/scan', LaserScan, self.lidar_update)

        self.rate = rospy.Rate(10)
        self.lidar_data = []

    def lidar_update(self, msg):
        self.lidar_data = msg.ranges

    def move(self):    
        vel_msg = Twist()    

        speed = 0.5

        #Since we are moving just in x-axis
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        
        while not rospy.is_shutdown():
            
            # find closest wall
            #TODO
            # turn right/left
            #TODO
            el = 0
            while True:

                # follow the wall at fixed distance
                #TODO
                # print(self.lidar_data)

                # if angle in front changes, stop and pivot
                #TODO

                vel_msg.linear.x = speed
                

                if len(self.lidar_data)>270:
                    half_range = 60
                    data = self.lidar_data[360-half_range:360]+self.lidar_data[0:half_range]

                    # decompose data into divisions
                    divs = int(half_range*2/20)                                         # number of divisions
                    divlength = int(len(data)/divs)                                     # therefore length of division
                    decomposed = list()                                                 # init list
                    # print(f"{len(data)=}\t{divs=}\t{divlength=}")
                    for i in range(0,divs):
                        decomposed.append( sum(data[i*divlength:(i+1)*divlength]) / divlength )   # decompose data 

                    # find max space
                    decmaxind = decomposed.index(max(decomposed))
                    dr = decmaxind-len(decomposed)/2

                    # find max space in that space
                    decmaxdat = data[decmaxind*divlength:(decmaxind+1)*divlength]
                    ddr = data.index(max(data))-half_range
                    kp = 0.5
                    kp2 = 0.05
                    print(kp2*sqrt(abs(ddr))*abs(ddr)/ddr)
                    vel_msg.angular.z = kp*dr+min(max(kp2*sqrt(abs(ddr))*abs(ddr)/ddr,-.2),.2)

                else:
                    vel_msg.angular.z = 0

                # drive toward max value in front
                
                # if len(self.lidar_data)>270:
                #     while min(self.lidar_data[0], self.lidar_data[180]) < min(self.lidar_data[90], self.lidar_data[270]):
                #         vel_msg.linear.x = 0
                #         vel_msg.angular.z = -1
                #         self.velocity_publisher.publish(vel_msg)
                #         self.rate.sleep()

                #     e = self.lidar_data[90]-self.lidar_data[270]
                #     de = el-e
                # else:
                #     e = el
                #     de = 0

                # kp = 2
                # kd = -1
                # vel_msg.angular.z = kp*e+kd*de       # +ve turns left
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move()
    except rospy.ROSInterruptException:
        pass
