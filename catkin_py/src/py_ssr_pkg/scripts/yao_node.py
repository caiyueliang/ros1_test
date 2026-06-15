#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('yao_topic_py')
    rospy.logwarn('[yao_topic_py] init_node success !')

    pub = rospy.Publisher('yao_topic_py', String, queue_size=10)
    rospy.logwarn('[yao_topic_py] publisher success !')

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = '[yao_topic_py] hello world'
        pub.publish(msg)
        rospy.logwarn('[yao_topic_py] publish msg success !')
        rate.sleep()