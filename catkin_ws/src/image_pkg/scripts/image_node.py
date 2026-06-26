#!/usr/bin/env python3
#coding=utf-8

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def Cam_RGB_callback(msg):
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        rospy.logerr(e)
        return

    # Display the image using OpenCV
    cv2.imshow("RGB Image", cv_image)
    cv2.waitKey(1)


 
if __name__ == '__main__':
    rospy.init_node('demo_cv_image')
    rospy.logwarn('[demo_cv_image] init_node success !')

    rgb_sub = rospy.Subscriber('/kinect2/qhd/image_color_rect', Image, Cam_RGB_callback, queue_size=10)
    
    rospy.spin()

    