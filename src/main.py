#!/usr/bin/env python3
import os
import time
import rospy
import threading
from sensor_msgs.msg import Image, CompressedImage # https://docs.ros.org/en/melodic/api/sensor_msgs/html/msg/Image.html

import flask
from flask import Flask, render_template, redirect, request, Response
from std_msgs.msg import String

#import html
# import requests

# https://iot-guider.com/raspberrypi/making-post-http-requests-with-python-flask/
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
# https://flask.palletsprojects.com/en/2.0.x/quickstart/

app = Flask(__name__)

# ROS node, publisher, and parameter.
# The node is started in a separate thread to avoid conflicts with Flask.
# The parameter *disable_signals* must be set if node is not initialized
# in the main thread.

threading.Thread(target=lambda: rospy.init_node('test_node', disable_signals=True)).start()
pubMotion = rospy.Publisher('/requestMotion01', String, queue_size=1)
pubStop = rospy.Publisher('/requestStop01', String, queue_size=1)
# NGROK = rospy.get_param('/ngrok', None)

# TODO maybe send as file instead of text
test_file = open("/home/synaptech/catkin_ws/src/ros_flask/src/testImg.txt", "r")
# plate_img = test_file.read()
start_msg_received = False # TODO only send the img if start message has been received

def send_start_message(msg):
    # r = requests.post('http://ada-feeding.ngrok.io', params={'q': 'raspberry pi request'})
    print('send start message')
    print(msg)
    start_msg_received = True
    # TODO finish implementing start message logic

def update_plate_img(received_img):
    print("updating img")
    # print(received_img.data)
    global plate_img
    # plate_img = "data:image/jpg;base64," + str(received_img)
    plate_img = str(received_img)


# subscribe to the start topic
rospy.Subscriber('start_capture', String, send_start_message)
# http://wiki.ros.org/rospy_tutorials/Tutorials/WritingImagePublisherSubscriber
rospy.Subscriber('/camera/color/image_raw/compressed', CompressedImage, update_plate_img)


@app.route('/')
def default():
    return "default route is working"

# send the image
@app.route('/img', methods=['GET'])
def send_img():
    print("got image request")
    print(request.data)
    while (plate_img == ""):
        time.sleep(1)

    # https://www.kite.com/python/answers/how-to-set-response-headers-using-flask-in-python
    response = flask.Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.data = plate_img
    return response

# get the image coordinates
@app.route('/coords', methods=['POST'])
def get_coords():
    print("x" + request.form['x'])
    print("y" + request.form['y'])

    # https://www.kite.com/python/answers/how-to-set-response-headers-using-flask-in-python
    response = flask.Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.data = "successfully received coordinates"
    return response
    # return 'successfully received coordinates'


# @app.route('/info')
# def info():
#     return html.info()


# @app.route('/send_movement_command/<direction>', methods = ['GET'])
# def send_movement_command(direction):
#     print("received command " + direction)
#     if any(direction in d for d in ['forward','backward','left','right', 'stop']):
#         # new ROSLIB.Message({data: motion})
#         if (direction == 'stop'):
#             pubStop.publish( direction.upper() )
#         else:
#             pubMotion.publish( direction.upper() )
#             return html.success(direction)
#     else:
#         mgs = 'Direction not recognized'
#         return html.failure(msg)


if __name__ == '__main__':
    # from og server
	app.run(host='0.0.0.0', debug=True)
