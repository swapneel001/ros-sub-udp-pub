#!/usr/bin/env python 
import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("cmdvel_publisher")
    message = Twist()
    message.linear.x = 2
    message.linear.y = 0
    message.linear.z = 3
    message.angular.x = 3
    pub = rospy.Publisher("cmd_vel",Twist, queue_size= 10)
    while not rospy.is_shutdown():
        pub.publish(message)

