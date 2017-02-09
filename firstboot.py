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

# set call for secondboot.py
f = open("/etc/rc.local","a")
f.write("sleep 10;python /home/pi/rpi_cnc_img/secondboot.py")
f.close

# reboot
sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])
