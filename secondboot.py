#!/usr/bin/env python
# secondboot.py
# call to the script gets placed in /etc/rc.local by firstboot.py
# ... and then removed by this script (so doesn't get called on every boot,
# just the first boot. The idea is to do basic settings in firstboot.py,
# and set the piscreen up, and then the majority of the RPi_cnc setup
# gets done in this script, when (hopefully) the LCD screen will show progress


import subprocess as sp
import os


# install zip/unzip
yesno = raw_input("Install zip/unzip? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "zip", "unzip", "-y"])

# install tightvncserver
yesno = raw_input("Install tightvncserver? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install","tightvncserver","-y"])

# install xrdp
yesno = raw_input("Install xrdp? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install","xrdp","-y"])

# install pip
yesno = raw_input("Install pip? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "python-pip", "-y"])

# install pyserial
yesno = raw_input("Install pyserial? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "pip", "install", "pyserial", "--upgrade", "-y"])

# install python
yesno = raw_input("Install python? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "python", "python-tk", "python-pmw", "python-imaging", "-y"])

# install arduino
yesno = raw_input("Install arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "arduino", "arduino-core", "arduino-mk", "-y"])

# install GRBL
# ****************** requires testing ****************************************
# **** if we are sure of the arduino directory, we can just use that, ********
# **** otherwise the sp.call(["locate"...]) and os.path.* functions   ********
# **** are intended to find it. **********************************************
# ****************************************************************************
yesno = raw_input("Install GRBL? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "updatedb"])  # update/build database for "locate" 
    # search for regex pattern for an arduino file
    arduinof = sp.call(["locate", "-br", "^arduino\.[0-9]*"])  # find file
    grbldir = os.path.dirname(os.path.abspath(arduinof)) + "/libraries/grbl"  # get path
    # sp.call(["wget", "https://github.com/Protoneer/GRBL-Arduino-Library/archive/master.zip"])
    grbldir = "/usr/share/arduino/libraries/grbl"
    sp.call(["sudo", "git", "clone","https://github.com/Protoneer/GRBL-Arduino-Library.git", grbldir])  # clone into specified directory
    sketch = open(grbldir + "/examples/Makefile","w")
    sketch.write("ARDUINO_DIR = /usr/share/arduino")
    sketch.write("BOARD_TAG = uno")
    sketch.write("ARDUINO_PORT = /dev/ttyACM*")  # not sure if "*" works
    sketch.write("ARDUINO_LIBS = include /usr/share/arduino/Arduino.mk")
    sketch.close()

# upload GRBL to Arduino
yesno = raw_input("Upload GRBL to Arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["cd",grbldir + "/examples"])
    # sp.call(["sudo", "make"])  # test that the sketch compiles
    sp.call(["sudo", "make", "upload"])  # upload to arduino
    # ***** alternative way - seems better *************
    sp.call(["arduino", "--upload", grbldir + "/examples/GRBLtoArduino.ino", "--port", "/dev/ttyUSB*"])  # check port name
    sp.call(["cd", "/home/pi"])

# clone bCNC
yesno = raw_input("Clone bCNC? (yes/no)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"])

# Create bCNC Desktop Shortcut 
yesno = raw_input("Create bCNC Desktop Shortcut? (y/n) ")
if yesno == "y" or debugmode == False:
    # sp.call(["mv", "/home/pi/rpi_cnc_img/bCNC.desktop", "/home/pi/Desktop/"])
    sp.call(["ln", "-s", "/home/pi/bCNC/bCNC.desktop", "/home/pi/Desktop/bCNC"])

# Download TeamViewer
yesno = raw_input("Install TeamViewer? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])

