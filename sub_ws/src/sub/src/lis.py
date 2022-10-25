#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix,Image
from darknet_ros_msgs.msg import BoundingBoxes
import message_filters
import nextcloud_client
import requests

#nc=nextcloud_client.Client('http://61.252.59.34:31014')
#nc.login('root','root')
lat=0
lon=0
obj_name=""
bridge=CvBridge()
def callback(data):
    lat=data.latitude
    lon=data.longitude
    print("lat:{}, lon:{}".format(lat,lon))
    

def callback2(data):
    print("receive image")
#    try:
#        cv2_img=bridge.imgmsg_to_cv2(data,"bgr8")
#    except CvBridgeError,e:
#        print(e)
#    else:
#        time=data.header.stamp
#        cv2.imwrite(''+str(time)+'.png',cv2_img)
#        nc.put_file('test/test{}.png'.format(time),img_name)
#        print('write')
#        os.remove(img_name)
#       link_info=nc.share_file_with_link('test/test{}.png'.format(time)).getlink()+"preview"
#   URL='http://103.218.163.29:3500/nodelinkapi/event?eventtype=etc&eventdetailtype='+obj_name+'&lat='+lat+'&lng='+lng+'&vehicle_id=31&image_path='+link_info+'&time'
def callback3(data):
    for i in data.bounding_boxes:
        obj_name+=str(i.id)
    print("{}".format(obj_name))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('ublox_gps/fix', NavSatFix, callback)
    #rospy.Subscriber('darknet_ros/detection_image',Image,callback2)
   # rospy.Subscriber('darknet_ros/bounding_boxes',BoundingBoxes,callback3)
    rospy.spin()

if __name__ == '__main__':
    listener()
