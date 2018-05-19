# -*- coding: utf-8 -*-
import argparse
import picamera
import os
import re

from pprint import pprint
from datetime import datetime

def camera():
    now = datetime.now()
    dir_name = now.strftime('%Y%m%d')
    dir_path = '/home/pi/AIY-projects-python/src/robot/image/' + dir_name + '/'
    file_name= now.strftime('%H%M%S') + '.jpg'
    fname    = dir_path + file_name
    try:
      os.mkdir(dir_path)
    except OSError:
      pprint('Date dir already exists')
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.capture(fname)
    return fname

def main(photo_file):
    if photo_file == "":
        photo_file = camera()
    result = photo_file
    return result

if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('image', nargs='?', default='', help='Image file name')
     args = parser.parse_args()
     result = main(args.image)
     pprint(result)


