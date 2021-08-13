# Repository : ros-sub-udp-pub

## This repository contains code to subscibe to /cmd_vel ros topic, and publish via UDP to localhost Port 9000

### Code launch sequence: 

*run each command in an individual tab*

'''
roscore
rosrun fyp pub.py
rosrun fyp sub.py
python udpsub.py
'''

### Functions for each program:
1. pub.py publishes a dummy message to /cmd_vel
2. sub.py subscribes to it, and publishes to localhost port 9000 via UDP
3. udpsub.py listens t the udp socket, and prints the message
4. udppubsubhandler is a handler file, doesnt need to be launched. 
