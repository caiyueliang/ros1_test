#!/usr/bin/env python3
#coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

count = 0

def lidar_callback(msg):
    global vel_cmd
    global count
      
    distance = msg.ranges[180]  # 前方距离
    rospy.loginfo(f"前方距离: {distance} 米")
    
    if count > 0:
        count -= 1
        return

    vel_cmd = Twist()
    if distance < 1.5:
        # 前方有障碍物
        rospy.logwarn("前方有障碍物")
        # vel_cmd.linear.x = 0.3
        vel_cmd.angular.z = 0.5
        count = 30
    else:
        # 前方没有障碍物
        rospy.loginfo("前方没有障碍物")
        vel_cmd.linear.x = 0.3
        vel_cmd.angular.z = 0.0

    vel_pub.publish(vel_cmd)


if __name__ == '__main__':
    rospy.init_node('lidar_node_py')
    rospy.logwarn('[lidar_node_py] init_node success !')

    lidar_sub = rospy.Subscriber('/scan', LaserScan, lidar_callback, queue_size=10)
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.logwarn('[lidar_node_py] publisher success !')

    rospy.spin()