#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp


debugmode = False  # if True, then requires a user prompt for every action

# Expand Filesystem
yesno = input("Expand Filesystem? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "raspi-config", "nonint", "do_expand_rootfs"])

# install zip/unzip
yesno = input("Install zip/unzip? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "zip", "unzip", "-y"])

# install xrdp
yesno = input("Install xrdp? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install","xrdp","-y"])

# install pip
yesno = input("Install pip? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "python-pip", "-y"])

# install pyserial
yesno = input("Install pyserial? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "pip", "install", "pyserial", "--upgrade", "-y"])

# install python
yesno = input("Install python? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "python", "python-tk", "python-pmw", "python-imaging", "-y"])

# install arduino
yesno = input("Install arduino? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "arduino", "arduino-core", "arduino-mk", "-y"])

# clone bCNC
yesno = input("Clone bCNC? (yes/no)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"])

# install TeamViewer
yesno = input("Install TeamViewer? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])

# install GRBL
yesno = input("Install GRBL? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "https://github.com/Protoneer/GRBL-Arduino-Library/archive/master.zip"])

# Create bCNC Desktop Shortcut 
yesno = input("Create bCNC Desktop Shortcut? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["mv", "/home/pi/rpi_cnc_img/bCNC.desktop", "/home/pi/Desktop/"])

# Enable arduino uploading
yesno = input("Enable Arduino uploading? (y/n)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])

#
