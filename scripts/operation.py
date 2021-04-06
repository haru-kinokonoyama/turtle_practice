#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

class Movement():
    def __init__(self):
        self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=1)

    def star_line(self):
        dist = 4.0
        speed = 2.0
        target_time = dist / speed

        t = Twist()
        t.linear.x = speed
        t.angular.z = 0

        start_time = time.time()
        end_time = time.time()

        rate = rospy.Rate(50)

        while end_time - start_time <= target_time:
            self.pub.publish(t)
            end_time = time.time()
            rate.sleep()

    def star_turn(self):
        theta = 144
        speed = 72
        target_time = theta / speed

        t = Twist()
        t.linear.x = 0
        t.angular.z = speed*3.14/180

        start_time = time.time()
        end_time = time.time()

        rate = rospy.Rate(50)

        while end_time - start_time <= target_time:
            self.pub.publish(t)
            end_time = time.time()
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('operation')
    movement = Movement()
    for i in range(5):
        movement.star_line()
        movement.star_turn()