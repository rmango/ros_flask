#!/usr/bin/env python3
import os
import rospy
import threading

from flask import Flask, render_template, redirect
from std_msgs.msg import String

#import html

app = Flask(__name__)

# ROS node, publisher, and parameter.
# The node is started in a separate thread to avoid conflicts with Flask.
# The parameter *disable_signals* must be set if node is not initialized
# in the main thread.

threading.Thread(target=lambda: rospy.init_node('test_node', disable_signals=True)).start()
pubMotion = rospy.Publisher('/requestMotion01', String, queue_size=1)
pubStop = rospy.Publisher('/requestStop01', String, queue_size=1)
# NGROK = rospy.get_param('/ngrok', None)


@app.route('/')
def default():
    return "hi"


# @app.route('/info')
# def info():
#     return html.info()


@app.route('/send_movement_command/<direction>', methods = ['GET'])
def send_movement_command(direction):
    if any(direction in d for d in ['forward','backward','left','right', 'stop']):
        # new ROSLIB.Message({data: motion})
        if (direction == 'stop'):
            pubStop.publish( direction.upper() )
        else:
            pubMotion.publish( direction.upper() )
            return html.success(direction)
    else:
        mgs = 'Direction not recognized'
        return html.failure(msg)


if __name__ == '__main__':
    # from og server
	app.run(host='0.0.0.0', debug=True)
