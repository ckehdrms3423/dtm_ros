#!/usr/bin/env python2
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

pub=rospy.Publisher('image',Image,queue_size=1)
rospy.init_node('talker',anonymous=True)
bridge=CvBridge()

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cap.set(cv2.CAP_PROP_FPS,30)
while not rospy.is_shutdown():
    ret,frame=cap.read()
    pub.publish(bridge.cv2_to_imgmsg(frame,"bgr8"))
    #print('send')
cap.release()
cv2.destroyAllWindows()
