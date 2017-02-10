#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp
import os
import helpy as h

debugmode = True  # if True, then requires a user prompt for every action

# INITIAL CONFIGS (BEFORE REBOOT)

# Enable arduino uploading
# requires reboot
yesno = raw_input("Enable Arduino uploading? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo usermod -a -G dialout pi")
#    sp.call(shellcmd.split())

# Enable PiScreenDrivers and configure calibration settings
# calibration steps come from http://ozzmaker.com/forums/topic/piscreen-raspberripi2-touchscreen-calibration/
yesno = raw_input("Enable Piscreen? (y/n) ")
if yesno == "y" or debugmode == False:
    #h.cmdcall("sudo sed -i """$ a\dtoverlay=piscreen,speed=16000000,rotate=90""" /boot/config.txt")
    sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=90", "/boot/config.txt"])
    # f = open("/boot/config.txt","a")
    # f.write("dtoverlay=piscreen,speed=16000000,rotate=90")
    # f.close
    #h.cmdcall("sed -i /^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axes (?i)Swap*$ /s/^/#/ /etc/X11/xinit/xinitrc")
    sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axes (?i)Swap*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    # sp.call(shellcmd.split())
    #h.cmdcall("sed -i /^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev Axis (?i)Inversion*$ /s/^/#/ /etc/X11/xinit/xinitrc")
    sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axis (?i)Inversion*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    # sp.call(shellcmd.split())
    if os.path.isfile("etc/pointercal.xinput"):
        h.cmdcall("sudo mv etc/pointercal.xinput etc/pointercal.xinput_copy")
        # sp.call(shellcmd.split())

# upgrade packages
yesno = raw_input("Upgrade packages? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude safe-upgrade -y")
#    sp.call(shellcmd.split())
#   sp.call(["sudo", "aptitude", "safe-upgrade"])

# set call for secondboot.py
f = open("/etc/rc.local","a")
f.write("sleep 10;python /home/pi/rpi_cnc_img/secondboot.py")
f.close
