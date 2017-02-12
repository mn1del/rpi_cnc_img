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


debugmode = False


# install tightvncserver
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install tightvncserver? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude install tightvncserver -y")
#    sp.call(["sudo", "aptitude", "install","tightvncserver","-y"])

# upgrade packages
# perhaps one for second boot?
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upgrade packages? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude safe-upgrade -y")
#    sp.call(shellcmd.split())
#   sp.call(["sudo", "aptitude", "safe-upgrade"])

# install zip/unzip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install zip/unzip? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude install zip unzip -y")
#    sp.call(["sudo", "aptitude", "install", "zip", "unzip", "-y"])

# install xrdp
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install xrdp? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude install xrdp -y")
#    sp.call(["sudo", "aptitude", "install","xrdp","-y"])

# install pip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pip? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude install python-pip -y")
#    sp.call(["sudo", "aptitude", "install", "python-pip", "-y"])

# install pyserial
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pyserial? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo pip install pyserial --upgrade")
#    sp.call(["sudo", "pip", "install", "pyserial", "--upgrade", "-y"])

# install python
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install python? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude install python python-tk python-pmw python-imaging -y")
#    sp.call(["sudo", "aptitude", "install", "python", "python-tk", "python-pmw", "python-imaging", "-y"])

# install arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("sudo aptitude install arduino arduino-core arduino-mk -y")
    h.cmdcall("sudo aptitude install gcc-avr avr-libc avrdude -y")
#    sp.call(["sudo", "aptitude", "install", "arduino", "arduino-core", "arduino-mk", "-y"])

# install GRBL and configure Makefile (which is the mechnism by which it gets uploaded to arduinio
# the actual uploading will be handled by another script because "cd'ing" into the directory is necessary
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install GRBL? (y/n) ")
if yesno == "y" or debugmode == False:
    grbldir = "/usr/share/arduino/libraries/grbl"
    h.cmdcall("sudo git clone https://github.com/Protoneer/GRBL-Arduino-Library.git " + grbldir)  # clone into specified directory
    sp.call(["sudo", "touch", grbldir + "/examples/GRBLtoArduino/Makefile"])
    sp.call(["sudo", "chmod", "777", grbldir + "/examples/GRBLtoArduino/Makefile"])
    sketch = open(grbldir + "/examples/GRBLtoArduino/Makefile","w")
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
    h.cmdcall("sudo git clone https://github.com/vlachoudis/bCNC.git")
#    sp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"])

# Create bCNC Desktop Shortcut 
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Create bCNC Desktop Shortcut? (y/n) ")
if yesno == "y" or debugmode == False:
    # sp.call(["mv", "/home/pi/rpi_cnc_img/bCNC.desktop", "/home/pi/Desktop/"])
    h.cmdcall("ln -s /home/pi/bCNC/bCNC.desktop /home/pi/Desktop/bCNC")
#    sp.call(["ln", "-s", "/home/pi/bCNC/bCNC.desktop", "/home/pi/Desktop/bCNC"])

# Download TeamViewer
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install TeamViewer? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("wget http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb")
#    sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])

# set call for everyboot.py
# replaces previous call for secondboot.py
sp.call(["sudo", "sed", "-i", "/cd \/home\/pi/,/^exit 0/{//!d}", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])

# Set up X Windows for the piscreen
sp.call(["sudo", "aptitude", "-y", "install", "x11-xserver-utils"])
sp.call(["sudo", "mv", "/home/pi/rpi_cnc_img/disableblank.sh", "/etc/X11/Xsession.d/"])
sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/disableblank.sh"])
sp.call(["sudo", "sed", "-i", "$ a\/etc/X11/Xsession.d/disableblank.sh", "/etc/xdg/lxsession/LXDE-pi/autostart"])

# set call for everyboot.py
#sp.call(["sudo", "sed", "-i", "$ a\sleep 10;python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])

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
    h.cmdcall("sudo shutdown -r")


