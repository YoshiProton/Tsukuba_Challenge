#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rosbag
import rospy
from sensor_msgs.msg import Image
from time import sleep
import argparse
import cv2
from cv_bridge import CvBridge, CvBridgeError


class D435Listener:
    def __init__(self):
        self.image_topic = '/device_0/sensor_1/Color_0/image/data'
        self.depth_topic = '/device_0/sensor_0/Depth_0/image/data'
        self.infrared_topic = '/device_0/sensor_0/Infrared_1/image/data'

        self.image_sub = rospy.Subscriber(self.image_topic, Image, self.image_callback)
        self.depth_sub = rospy.Subscriber(self.depth_topic, Image, self.depth_callback)
        self.infrared_sub = rospy.Subscriber(self.infrared_topic, Image, self.ir_callback)
        self.bridge = CvBridge()
    
    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        #cv2.imshow('image', cv_image)
        #cv2.waitKey(1)

    def depth_callback(self, data):
        try:
            cv_depthimage = self.bridge.imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)
        #cv2.imshow('image', cv_depthimage)
        #cv2.waitKey(1)

    def ir_callback(self, data):
        try:
            cv_irimage = self.bridge.imgmsg_to_cv2(data, "passthrough")
        except CvBridgeError as e:
            print(e)
        #cv2.imshow('image', cv_irimage)
        #cv2.waitKey(1)

if __name__ == '__main__':
    rospy.init_node('d435_listener', anonymous=True)
    listener = D435Listener()

    try:
        rospy.spin()
    except KeyboardInterrupt:
	pass
    cv2.destroyAllWindows()


