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
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Enable Arduino uploading? (y/n) ")
if yesno == "y":
    sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])

# Enable PiScreenDrivers and configure for console use
# http://ozzmaker.com/enable-console-on-piscreen/
# calibration steps come from http://ozzmaker.com/forums/topic/piscreen-raspberripi2-touchscreen-calibration/
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Enable Piscreen? (y/n) ")
if yesno == "y":
    sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=270", "/boot/config.txt"])
    # for boot to CLI:
    sp.call(["cp", "/boot/cmdline.txt", "/home/pi/cmdline.txt"])   # backup cmdline.txt
    sp.call(["sudo", "sed", "-i", "1 s/$/ fbcon=map:10 fbcon=rotate:2 fbcon=font:ProFont6x11/", "/boot/cmdline.txt"])

    #sp.call(
    #sp.call(["sudo", "aptitude", "-y", "install", "x11-xserver-utils"])  # install X server utilities
    #sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axes (?i)Swap*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    #sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axis (?i)Inversion*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])

    #if os.path.isfile("etc/pointercal.xinput"):
        #h.cmdcall("sudo mv etc/pointercal.xinput etc/pointercal.xinput_copy")

# set call for secondboot.py
sp.call(["sudo", "sed", "-i", "/^exit 0/i \cd /home/pi", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \sleep 10;python /home/pi/rpi_cnc_img/secondboot.py", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \cd /usr/share/arduino/libraries/grbl/examples/GRBLtoArduino", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \python /home/pi/rpi_cnc_img/secondboot_arduino.py", "/etc/rc.local"])

# reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Reboot? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "shutdown", "-r"])

