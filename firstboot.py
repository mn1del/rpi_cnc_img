#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp


debugmode = True  # if True, then requires a user prompt for every action

# Expand Filesystem
yesno = raw_input("Expand Filesystem? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "raspi-config", "nonint", "do_expand_rootfs"])

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

# clone bCNC
yesno = raw_input("Clone bCNC? (yes/no)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"])

# install TeamViewer
yesno = raw_input("Install TeamViewer? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])

# install GRBL
yesno = raw_input("Install GRBL? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "https://github.com/Protoneer/GRBL-Arduino-Library/archive/master.zip"])

# Create bCNC Desktop Shortcut 
yesno = raw_input("Create bCNC Desktop Shortcut? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["mv", "/home/pi/rpi_cnc_img/bCNC.desktop", "/home/pi/Desktop/"])

# Enable arduino uploading
yesno = raw_input("Enable Arduino uploading? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])

# Enable PiScreenDrivers
f = open("/boot/config.txt","a")
f.write("dtoverlay=piscreen,speed=16000000,rotate=90")
f.close
