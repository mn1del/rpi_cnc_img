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
    log = sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=270", "/boot/config.txt"])
    bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "$ a\dtoverlay=piscreen,speed=16000000,rotate=270", "/boot/config.txt"])')
    bootlog.write(log)
    bootlog.write("\n")
    # for boot to CLI:
    log = sp.call(["cp", "/boot/cmdline.txt", "/home/pi/cmdline.txt"])   # backup cmdline.txt
    bootlog.write('\nlog = sp.call(["cp", "/boot/cmdline.txt", "/home/pi/cmdline.txt"])   # backup cmdline.txt')
    bootlog.write(log)
    bootlog.write("\n")

    log = sp.call(["sudo", "sed", "-i", "1 s/$/ fbcon=map:10 fbcon=rotate:2 fbcon=font:ProFont6x11/", "/boot/cmdline.txt"])
    bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "1 s/$/ fbcon=map:10 fbcon=rotate:2 fbcon=font:ProFont6x11/", "/boot/cmdline.txt"])')
    bootlog.write(log)
    bootlog.write("\n")

    #log = sp.call(
    #log = sp.call(["sudo", "aptitude", "-y", "install", "x11-xserver-utils"])  # install X server utilities
    #log = sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axes (?i)Swap*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    #log = sp.call(["sudo", "sed", "-i", "/^DISPLAY=*xinput*(?i)Touchscreen*(?i)Evdev (?i)Axis (?i)Inversion*$ /s/^/#/", "/etc/X11/xinit/xinitrc"])
    log = sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])
    bootlog.write('\nlog = sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])')
    bootlog.write(log)
    bootlog.write("\n")

    #if os.path.isfile("etc/pointercal.xinput"):
        #h.cmdcall("sudo mv etc/pointercal.xinput etc/pointercal.xinput_copy")

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

