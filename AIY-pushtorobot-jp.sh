#!/bin/bash --rcfile

source /etc/bash.bashrc
source ~/.bashrc

cat /etc/aiyprojects.info

cd ~/AIY-projects-python

echo "Dev terminal is ready! See the demos in 'src/examples' to get started."

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/AIY-projects-python/src/robot/vision.json

echo "Google Pushtotalk ja-JP is running!"

python3 /home/pi/AIY-projects-python/src/robot/pushtorobot.py --device-model-id aiy-prj-device1 --project-id aiy-prj --device-id 5AF12EEF9DD8DFD80274F27D306143B0 --lang ja-JP

