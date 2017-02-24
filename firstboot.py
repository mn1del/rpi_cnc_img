#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp
import os
#import helpy as h

debugmode = False  # if True, then requires a user prompt for every action
bootlog = open("/home/pi/bootlog.txt", "w")  # creat log file to track boot script progress


# INITIAL CONFIGS (BEFORE REBOOT)

# Enable arduino uploading
# requires reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Enable Arduino uploading? (y/n) ")
if yesno == "y":
    log = sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])
    bootlog.write('\nlog = sp.call(["sudo", "usermod", "-a", "-G", "dialout", "pi"])')
    bootlog.write(log)
    bootlog.write("\n")

# Enable PiScreenDrivers and configure for console use
# http://ozzmaker.com/enable-console-on-piscreen/
# calibration steps come from http://ozzmaker.com/forums/topic/piscreen-raspberripi2-touchscreen-calibration/
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Enable Piscreen? (y/n) ")
if yesno == "y":
    # enable PiScreen
    log = sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=270", "/boot/config.txt"])
    bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=270", "/boot/config.txt"])')
    bootlog.write(log)
    bootlog.write("\n")

    #FOR BOOT TO COMMAND LINE
    log = sp.call(["cp", "/boot/cmdline.txt", "/home/pi/cmdline.txt"])   # backup cmdline.txt
    bootlog.write('\nlog = sp.call(["cp", "/boot/cmdline.txt", "/home/pi/cmdline.txt"])   # backup cmdline.txt')
    bootlog.write(log)
    bootlog.write("\n")
    # configure correct orientation
    log = sp.call(["sudo", "sed", "-i", "1 s/$/ fbcon=map:10 fbcon=rotate:2 fbcon=font:ProFont6x11/", "/boot/cmdline.txt"])
    bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "1 s/$/ fbcon=map:10 fbcon=rotate:2 fbcon=font:ProFont6x11/", "/boot/cmdline.txt"])')
    bootlog.write(log)
    bootlog.write("\n")

    # output display to GPIO (PiScreen)
    log = sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])
    bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])')
    bootlog.write(log)
    bootlog.write("\n")

    # disable screen blanking (just once)
    sp.call(["sudo", "xset", "s", "off"])
    sp.call(["sudo", "xset", "-dpms"])
    sp.call(["sudo", "xset", "s", "noblank"])
    # disable screen balnking permanently (uncomment to effect this)
    # sp.call(["sudo", "sed", "-i", "/[sS]eat*[dD]efaults/ a\xserver-command=X -s 0 -dpms", "/etc/lightdm/lightdm.conf"])

# set call for secondboot.py
log = sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sleep 10;python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])
bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sleep 10;python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])')
bootlog.write(log)
bootlog.write("\n")

# reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Reboot? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "shutdown", "-r"])

