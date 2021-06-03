## UPDATED DOCS

This is a ros package, so needs to go inside of the src of a catkin workspace
remember to `pip install Flask`

to run: `roslaunch ros_flask start_server.launch`
also run the start message ros python file, in this repo: https://github.com/rmango/ROS-arm-cam

for camera topic: `rosrun image_transport republish raw in:=/camera/color/image_raw compressed out:=/camera/color/image_raw`  

## Running with a rosbag
In a new terminal, cd into the directory that contains your rosbag\
run ```$ source /opt/ros/noetic/setup.bash```\
run ```$ rosbag play <rosbag_name>.bag```

# Testing
To test out messages, use [Postman](https://www.postman.com/)  
example postman requests are in the file research.postman_collection.json

Helpful command to watch the /img_coord topic: `rostopic echo /img_coords`

** old docs start here **
------------
# About

Simple Flask - ROS prototype.

Alternative to using [ROSLIBJS](http://wiki.ros.org/roslibjs)

Send motion commands via `http://localhost:5000/send_movement_command/<direction>`

View possible commands at `http://localhost:5000/help`

An in-depth tutorial is available on the [ros_flask wiki](https://github.com/stoddabr/ros_flask/wiki/Tutorial)

# Basic Quickstart

After setting up ROS catkin and making, run this:
```bash
roslaunch flask_ros start_server.launch
```

For more information view the flask_ask_ros repo linked below.

# Limitations

* Flask HTML templates don't seem to work.
See /src/html.py for used workaround for providing html responses.
This could be an issue with how ROS manages directories. -- NOTE: I have actually fixed this on another project but am too lazy to update things here. If someone wants this create an issue and I'll update this repo

# Acknowledgements

originally cloned from this repo by the [3Spheres Project](https://3srp.com/):
  https://github.com/3SpheresRoboticsProject/flask_ask_ros

found from this article which explains why this works:
  https://campus-rover.gitbook.io/lab-notebook/cr-package/web-application/flask-and-ros

for use in Oregon State University's Charisma Lab:
  https://www.charismarobotics.com/
