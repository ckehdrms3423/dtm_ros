# dtm_ros
  roscore
  ## usb_ws
    USB cam ros
     
     USB cam 변수 명 확인
      ls -ltr /dev/video*
      
![스크린샷, 2022-10-12 10-21-54](https://user-images.githubusercontent.com/49112411/195227704-60f4d44c-73b8-41b7-8ccd-c1dab0c1b555.png)

      새로 생긴 video3 or 2를
      
      vi src/usb_cam/launch/usb_cam-test.launch
        param name="video_device" value="dev/video( )" 숫자 변경
        
      vi src/usb_cam/nodes/usb_cam_node.cpp
        node_.param("video_device",video_device_name_,std::string("/dev/video( )")); 숫자 변경
        
     catkin_make
     source devel/setup.bash
     
     roslaunch usb_cam usb_cam-test.launch
  ## gps_ws
  
    catkin_make
    source devel/setup.bash
    
    roslaunch ublox_gps ublox_device.launch
  ## rosbag
    rosbag record -a -X "(.*)/compressed(.*)" -O "bagfilename"
