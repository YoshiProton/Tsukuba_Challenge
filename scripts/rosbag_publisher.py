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


class D435Publisher:
    def __init__(self):
	current_path = os.path.dirname(os.path.abspath(__file__))
	self.bag_path = os.path.join(current_path, '20180630_141001.bag')
	
        self.image_topic = '/device_0/sensor_1/Color_0/image/data'
        self.depth_topic = '/device_0/sensor_0/Depth_0/image/data'
        self.infrared_topic = '/device_0/sensor_0/Infrared_1/image/data'

        self.image_pub = rospy.Publisher(self.image_topic, Image, queue_size=10)
        self.depth_pub = rospy.Publisher(self.depth_topic, Image, queue_size=10)
        self.infrared_pub = rospy.Publisher(self.infrared_topic, Image, queue_size=10)
        self.bridge = CvBridge()

    def read(self):
        r = rospy.Rate(10)
        index = 0

        with rosbag.Bag(self.bag_path) as bag:
            for topic, msg, t in bag.read_messages(topics=[self.image_topic, self.depth_topic, self.infrared_topic]):
                if topic == self.image_topic:
                    self.image_pub.publish(msg)
                if topic == self.depth_topic:
                    self.depth_pub.publish(msg)
                if topic == self.infrared_topic:
                    self.infrared_pub.publish(msg)
                rospy.sleep(0.1)

def main():
    rospy.init_node("d435_publisher", anonymous=True, disable_signals=True)
    publisher = D435Publisher()
    publisher.read()
    rospy.spin()


if __name__ == "__main__":
    main()
