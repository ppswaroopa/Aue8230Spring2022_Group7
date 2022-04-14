from geometry_msgs.msg import Twist
from move_robot import MoveTurtlebot3
from apriltag_ros.msg import AprilTagDetectionArray
import rospy

at_x = 0
at_z = 0
def april_tag_callback(data):
    # update data in case apriltag is detected
    # if no apriltag detected, make bool false, so botcontrol() is used instead

    global apriltagdetected
    if len(data.detections) > 0:
        apriltagdetected = True

        # make target 
        global at_x
        global at_z
        at_x = data.detections[0].pose.pose.pose.position.x
        at_z = data.detections[0].pose.pose.pose.position.z
        # print(f"{at_x=}\t{at_z=}")
        
    else:
        # conditions to do nothing, commented because the boolean variable will disable execution of follow_apriltag()
        # at_x = 0.5
        # at_z = 0.5
        apriltagdetected = False

def clip(val, mx, mn=None):
    # clip val to range (mn, mx)
    # if mn not defined, clip val to range (-mx, mx)

    if mn == None:
        return max(-mx, min(val, mx))
    return max(mn, min(val, mx))

def follow_apriltag():
    april_tag_sub = rospy.Subscriber("/tag_detections", AprilTagDetectionArray, april_tag_callback)
    mv_object = rospy.Publisher('/cmd_vel', Twist)

    # parameters for motion
    v_max = 0.25
    v_mul = 1.2
    a_max = 0.5
    a_mul = 2.8

    distance_target = 0.5
    
    # define and calculate message
    cmd = Twist()
    cmd.linear.x = clip((at_z-distance_target)*v_mul, v_max)
    cmd.angular.z = clip(-at_x*a_mul, a_max)

    print(f"{cmd.linear.x=}\t{cmd.angular.z=}")

    # Make it start turning
    # moveTurtlebot3_object.move_robot(cmd)
    mv_object.publish(cmd)

    return
