#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp
import os

debugmode = True  # if True, then requires a user prompt for every action

# INITIAL CONFIGS (BEFORE REBOOT)

# Expand Filesystem
yesno = raw_input("Expand Filesystem? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "raspi-config", "nonint", "do_expand_rootfs"])

# Enable arduino uploading
# requires reboot
yesno = raw_input("Enable Arduino uploading? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])

# Enable PiScreenDrivers and configure calibration settings
# calibration steps come from http://ozzmaker.com/forums/topic/piscreen-raspberripi2-touchscreen-calibration/
f = open("/boot/config.txt","a")
f.write("dtoverlay=piscreen,speed=16000000,rotate=90")
f.close
sp.call(["sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axes (?i)Swap*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
sp.call(["sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axis (?i)Inversion*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
sp.call(["sudo", "mv", "etc/pointercal.xinput", "etc/pointercal.xinput_copy"])

# upgrade packages
yesno = raw_input("Upgrade packages? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "safe-upgrade"])

# ******* REBOOT HERE, then requires follow up first boot script *************


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

