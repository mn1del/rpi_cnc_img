#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp
import os
import helpy as h

debugmode = False  # if True, then requires a user prompt for every action

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
    sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=90", "/boot/config.txt"])
    sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axes (?i)Swap*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axis (?i)Inversion*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])

    if os.path.isfile("etc/pointercal.xinput"):
        h.cmdcall("sudo mv etc/pointercal.xinput etc/pointercal.xinput_copy")

# remove unnecessary packages
yesno = raw_input("Remove unnecessary packages? (y/n) ")
if yesno == "y" or debugmode == False:
#    h.cmdcall("sudo aptitude -y remove wolfram-engine penguinspuzzle scratch dillo squeak-vm squeak-plugins-scratch sonic-pi idle idle3 netsurf-gtk netsurf-common")

# set call for secondboot.py
#sp.call(["sudo", "sed", "-i", "$ a\sleep 10;python /home/pi/rpi_cnc_img/secondboot.py", "/etc/rc.local"])
#f = open("/etc/rc.local","a")
#f.write("sleep 10;python /home/pi/rpi_cnc_img/secondboot.py")
#f.close
