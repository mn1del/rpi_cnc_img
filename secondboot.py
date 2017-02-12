#!/usr/bin/env python
# secondboot.py
# call to the script gets placed in /etc/rc.local by firstboot.py
# ... and then removed by this script (so doesn't get called on every boot,
# just the first boot. The idea is to do basic settings in firstboot.py,
# and set the piscreen up, and then the majority of the RPi_cnc setup
# gets done in this script, when (hopefully) the LCD screen will show progress


import subprocess as sp
import os
import helpy as h


debugmode = True

# remove unnecessary packages
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Remove unnecessary packages? (y/n) ")
    if yesno == "y" or debugmode == False:
        sp.call(["sudo", "aptitude", "-y", "remove", "wolfram-engine", "penguinspuzzle", "dillo", "squeak-vm", "squeak-plugins-scratch", "sonic-pi", "netsurf-gtk", "netsurf-common"])

# install tightvncserver
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install tightvncserver? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install","tightvncserver","-y"])

# upgrade packages
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upgrade packages? (y/n) ")
if yesno == "y" or debugmode == False:
    #sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "safe-upgrade", "-y"])
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "safe-upgrade"])  

# install zip/unzip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install zip/unzip? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "zip", "unzip", "-y"])

# install xrdp
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install xrdp? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install","xrdp","-y"])

# install pip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pip? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "python-pip", "-y"])

# install pyserial
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pyserial? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "pip", "install", "pyserial", "--upgrade"])

# install python
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install python? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "python", "python-tk", "python-pmw", "python-imaging", "-y"])

# install arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install", "arduino", "arduino-core", "arduino-mk", "-y"])
    sp.call(["sudo", "aptitude", "install", "gcc-avr", "avr-libc", "avrdude", "-y"])

# install GRBL and configure Makefile (which is the mechnism by which it gets uploaded to arduinio
# the actual uploading will be handled by another script because "cd'ing" into the directory is necessary
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install GRBL? (y/n) ")
if yesno == "y" or debugmode == False:
    grbldir = "/usr/share/arduino/libraries/grbl"
    h.cmdcall("sudo git clone https://github.com/Protoneer/GRBL-Arduino-Library.git " + grbldir)  # clone into specified directory
    grbldir = grbldir + "/examples/GRBLtoArduino/Makefile"
    sp.call(["sudo", "touch", grbldir])
    sp.call(["sudo", "chmod", "777", grbldir])
    sketch = open(grbldir,"w")
    sketch.write("ARDUINO_DIR = /usr/share/arduino\n")
    sketch.write("BOARD_TAG = uno\n")
    sketch.write("ARDUINO_PORT = /dev/ttyACM0\n")
    sketch.write("ARDUINO_LIBS = grbl\n")
    sketch.write("include /usr/share/arduino/Arduino.mk\n")
    sketch.close()

# clone bCNC
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Clone bCNC? (yes/no)")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"])

# Create bCNC Desktop Shortcut 
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Create bCNC Desktop Shortcut? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["ln", "-s", "/home/pi/bCNC/bCNC.desktop", "/home/pi/Desktop/bCNC"])

# Download TeamViewer
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install TeamViewer? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])

# set call for everyboot.py
# replaces previous call for secondboot.py
sp.call(["sudo", "sed", "-i", "/cd \/home\/pi/,/^exit 0/{//!d}", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])

# Set up X Windows for the piscreen
sp.call(["sudo", "aptitude", "-y", "install", "x11-xserver-utils"])
sp.call(["sudo", "mv", "/home/pi/rpi_cnc_img/disableblank.sh", "/etc/X11/Xsession.d/"])
sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/disableblank.sh"])
sp.call(["sudo", "sed", "-i", "$ a\/etc/X11/Xsession.d/disableblank.sh", "/etc/xdg/lxsession/LXDE-pi/autostart"])

# set login to GUI autologin
#auto login
sp.call(["sudo", "sed", "-i", "s/1:12345:respawn:\/sbin\/getty 115200 tty1/1:2345:respawn:\/bin\/login -f pi tty1 <\/dev\/tty1 >\/dev\/tty1 2>&1/", "/etc/rc.local"])
#auto startx
sp.call(["sudo", "sed", "-i", "/^exit 0/i \sudo startx", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])

# reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Reboot? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "shutdown", "-r"])
