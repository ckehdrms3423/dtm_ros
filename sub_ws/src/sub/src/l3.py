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

#nc=nextcloud_client.Client('http://61.252.59.34:31014')
#nc.login('root','root')
lat=0
lon=0
#bridge=CvBridge()

def callback(fix,image,boxes):
    print("callback")
    lat=fix.latitude
    lon=fix.longitude
    link_info=""
    print("lat:{}, lon:{}".format(lat,lon))
    try:
        cv2_img=bridge.imgmsg_to_cv2(image,"bgr8")
    except CvBridgeError,e:
        print(e)
    else:
        time=image.header.stamp
        img_name="{}.png".format(time)
#        cv2.imwrite(img_name,cv2_img)
#        nc.put_file('test/test{}.png'.format(time),img_name)
        prient('{}write'.format(img_name))
#        os.remove(img_name)
#        link_info=nc.share_file_with_link('test/test{}.png'.format(time)).getlink()+"/preview"
#    print("{}".format(ObjectCount.Class))


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
