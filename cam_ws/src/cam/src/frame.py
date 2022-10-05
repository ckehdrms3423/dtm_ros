#!/usr/bin/env python3.7
import cv2
import numpy as np
import serial
import rospy
from std_msgs.msg import String
do=dict()
pub=rospy.Publisher('object',String,queue_size=15)
rospy.init_node('talker',anonymous=True)
cap=cv2.VideoCapture(0)
YOLO_net=cv2.dnn.readNet("/home/idp-503/cam_ws/src/cam/src/yolov4-tiny.weights","/home/idp-503/cam_ws/src/cam/src/yolov4-tiny.cfg")
classes=[]
with open("/home/idp-503/cam_ws/src/cam/src/coco.names","r") as f:
    classes=[line.strip() for line in f.readlines()]
def st_data(add,data):
    do[data]=add
for i in range(len(classes)):
    st_data(i,classes[i])

layer_names=YOLO_net.getLayerNames()
output_layers=[layer_names[i-1]for i in YOLO_net.getUnconnectedOutLayers()]
obj_name=""
o_st=0

while True:
    ret,frame=cap.read()
    h,w,c=frame.shape
    blob=cv2.dnn.blobFromImage(frame,0.00392,(416,416),(0,0,0),True,crop=False)
    YOLO_net.setInput(blob)
    outs=YOLO_net.forward(output_layers)

    class_ids=[]
    confidences=[]
    boxes=[]

    for out in outs:
        for detection in out:
            scores=detection[5:]
            class_id=np.argmax(scores)
            confidence=scores[class_id]

            if confidence>0.5:
                center_x=int(detection[0]*w)
                center_y=int(detection[1]*h)
                dw=int(detection[2]*w)
                dh=int(detection[3]*h)
                x=int(center_x-dw/2)
                y=int(center_y-dh/2)
                boxes.append([x,y,dw,dh])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.45,0.4)
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h=boxes[i]
            label=str(classes[class_ids[i]])
            score=confidences[i]

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
            cv2.putText(frame,label,(x,y-29),cv2.FONT_ITALIC,0.5,(255,255,255),1)
            if i==0:
                o_st=do[label]
            if i!=(len(boxes)-1):
                obj_name=obj_name+str(do[label])+','
            else:
                obj_name=obj_name+str(do[label])
#    rospy.loginfo(obj_name)
    pub.publish(obj_name)
