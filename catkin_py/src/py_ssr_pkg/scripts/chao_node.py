#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('chao_node')
    rospy.logwarn('chao_node init_node success !')

    pub = rospy.Publisher('chao_topic', String, queue_size=10)
    rospy.logwarn('chao_node publisher success !')

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = '[chao_node] hello world'
        pub.publish(msg)
        rospy.logwarn('chao_node publish msg success !')
        rate.sleep()