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
    h.cmdcall("sudo pip install pyserial --upgrade -y")
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
#    sp.call(["sudo", "aptitude", "install", "arduino", "arduino-core", "arduino-mk", "-y"])

# install GRBL
# ****************** requires testing ****************************************
# **** if we are sure of the arduino directory, we can just use that, ********
# **** otherwise the sp.call(["locate"...]) and os.path.* functions   ********
# **** are intended to find it. **********************************************
# ****************************************************************************
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install GRBL? (y/n) ")
if yesno == "y" or debugmode == False:
    grbldir = "/usr/share/arduino/libraries/grbl"
    h.cmdcall("sudo git clone https://github.com/Protoneer/GRBL-Arduino-Library.git" + grbldir)  # clone into specified directory
    sketch = open(grbldir + "/examples/Makefile","w")
    sketch.write("ARDUINO_DIR = /usr/share/arduino")
    sketch.write("BOARD_TAG = uno")
    sketch.write("ARDUINO_PORT = /dev/ttyACM*")  # not sure if "*" works
    sketch.write("ARDUINO_LIBS = include /usr/share/arduino/Arduino.mk")
    sketch.close()

# upload GRBL to Arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upload GRBL to Arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    h.cmdcall("cd " + grbldir + "/examples")
    h.cmdcall("sudo make")  # test that the sketch compiles
    h.cmdcall("sudo make upload")  # upload to arduino
    # ***** alternative way - seems better *************
    # sp.call(["arduino", "--upload", grbldir + "/examples/GRBLtoArduino.ino", "--port", "/dev/ttyUSB*"])  # check port name
    h.cmdcall("cd /home/pi")

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
sp.call(["sudo", "sed", "-i", "s/secondboot\.py/everyboot\.py/", "/etc/rc.local"])
#h.cmdcall("sed -i s/secondboot\.py/everyboot\.py /etc/rc.local")
# f = open("/etc/rc.local","a")
# f.write("sleep 10;python /home/pi/rpi_cnc_img/secondboot.py")
# f.close

# Set up X Windows for the piscreen
sp.call(["sudo", "aptitude", "-y", "install", "x11-xserver-utils"])
sp.call(["sudo", "mv", "/home/pi/rpi_cnc_img/diableblank.sh", "/etc/X11/Xsession.d/"])
sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/disableblank.sh"])
sp.call(["sudo", "sed", "-i", "$ a\/etc/X11/Xsession.d/disableblank.sh", "/etc/xdg/lxsession/LXDE-pi/autostart"])

# set call for everyboot.py
sp.call(["sudo", "sed", "-i", "$ a\sleep 10;python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])

# set login to GUI autologin
#auto login
sp.call(["sed", "-i", "s/1:12345:respawn:\/sbin\/getty 115200 tty1/1:2345:respawn:\/bin\/login -f pi tty1 <\/dev\/tty1 >\/dev\/tty1 2>&1", "/etc/rc.local"])
#auto startx
sp.call(["sudo", "sed", "-i", "/exit 0/i \sudo -l pi -c startx", "/etc/rc.local"])

# reboot
#if debugmode == False:
#    yesno = "y"
#else:
#    yesno = raw_input("Reboot? (y/n) ")
#if yesno == "y" or debugmode == False:
#    h.cmdcall("sudo shutdown -r")


