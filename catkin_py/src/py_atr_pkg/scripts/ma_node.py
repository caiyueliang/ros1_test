#!/usr/bin/env python3
#coding=utf-8

import rospy
from std_msgs.msg import String

def yao_callback(msg):
    rospy.logwarn('[ma_topic_py] yao_callback msg: %s', msg.data)

def chao_callback(msg):
    rospy.loginfo('[ma_topic_py] chao_callback msg: %s', msg.data)



if __name__ == '__main__':
    rospy.init_node('ma_topic_py')
    rospy.logwarn('[ma_topic_py] init_node success !')

    sub_yao = rospy.Subscriber('yao_topic_py', String, yao_callback, queue_size=10)
    sub_chao = rospy.Subscriber('chao_topic_py', String, chao_callback, queue_size=10)

    rospy.spin()

    