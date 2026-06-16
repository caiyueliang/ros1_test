#!/usr/bin/env python3
#coding=utf-8

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('vel_node_py')
    rospy.logwarn('[vel_node_py] init_node success !')

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.logwarn('[vel_node_py] publisher success !')

    vel_msg = Twist()
     
    vel_msg.linear.x = 0.5
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.5

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()