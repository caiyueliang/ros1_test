#!/usr/bin/env python3
#coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan

def lidar_callback(msg):
    distance = msg.ranges[180]  # 前方距离
    rospy.loginfo(f"前方距离: {distance} 米")
    if distance < 1.0:
        # 前方有障碍物
        rospy.logwarn("前方有障碍物")
    else:
        # 前方没有障碍物
        rospy.loginfo("前方没有障碍物")
    # rospy.loginfo(msg.ranges)
    # rospy.loginfo(msg.angle_min)
    # rospy.loginfo(msg.angle_max)
    # rospy.loginfo(msg.angle_increment)
    # rospy.loginfo(msg.range_min)
    # rospy.loginfo(msg.range_max)
    # rospy.loginfo(msg.scan_time)


if __name__ == '__main__':
    rospy.init_node('lidar_node_py')
    rospy.logwarn('[lidar_node_py] init_node success !')

    lidar_sub = rospy.Subscriber('/scan', LaserScan, lidar_callback, queue_size=10)

    rospy.spin()