#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
rospy.init_node('operation')
pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1)
rate = rospy.Rate(1)

t = Twist()
t.linear.x = 2.0
t.angular.z = -1.8

while not rospy.is_shutdown():
    pub.publish(t)
    rate.sleep()

    