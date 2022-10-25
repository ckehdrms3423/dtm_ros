#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix,Image
from darknet_ros_msgs.msg import BoundingBoxes
import message_filters

lat=0
lon=0
#bridge=CvBridge()

def callback(ublox_gps/fix,darknet_ros/detection_image,Image):
    print("callback")
    lat=NavSatFix.latitude
    lon=NavSatFix.longitude
    print("lat:{}, lon:{}".format(lat,lon))
#    try:
#        cv2_img=bridge.imgmsg_to_cv2(data,"bgr8")
#    except CvBridgeError,e:
#        print(e)#
#   else:
#        time=data.header.stamp
#        cv2.imwrite(''+str(time)+'.png',cv2_img)
#        print('write')
    print("{}".format(ObjectCount.Class))

def listener():
    rospy.init_node('listener',anonymous=True)
    gps_sub=message_filters.Subscriber('ublox_gps/fix',NavSatFix)
    image_sub=message_filters.Subscriber('darknet_ros/detection_image',Image)
    object_sub=message_filters.Subscriber('darknet_ros/bounding_boxes',BoundingBoxes)
    ts=message_filters.ApproximateTimeSynchronizer([gps_sub,image_sub,object_sub],10,0.5)
    ts.registerCallback(callback)
    print("spin")
    #rospy.spin()
    

if __name__ == '__main__':
    filter_listener = listener()
    rospy.spin()
