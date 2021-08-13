#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from udppubsubhandler import Pub

def callback(msg):
    publisher = Pub()
    message = str(msg.linear.x) + " , " + str(msg.angular.x)
    print ("message : ", message)
    publisher.send(message)

def listener():
    rospy.Subscriber("/cmd_vel",Twist,callback)
    rospy.spin()
if __name__ == "__main__":
    rospy.init_node('cmd_vel_transmitter')
    listener()