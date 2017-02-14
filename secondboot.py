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

# remove unnecessary packages
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Remove unnecessary packages? (y/n) ")
    if yesno == "y" or debugmode == False:
        sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""","remove", "wolfram-engine", "penguinspuzzle", "dillo", "squeak-vm", "squeak-plugins-scratch", "sonic-pi", "netsurf-gtk", "netsurf-common"])

# install tightvncserver
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install tightvncserver? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::='--force-confdef'", "-o", "Dpkg::Options::=""--force-confold""",  "install","tightvncserver"])

# upgrade packages
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upgrade packages? (y/n) ")
if yesno == "y" or debugmode == False:
    #sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "safe-upgrade"])
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "safe-upgrade"])  

# install zip/unzip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install zip/unzip? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "zip", "unzip"])

# install xrdp
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install xrdp? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install","xrdp"])

# install pip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pip? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "python-pip"])

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
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "python", "python-tk", "python-pmw", "python-imaging"])

# install arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "arduino", "arduino-core", "arduino-mk"])
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "gcc-avr", "avr-libc", "avrdude"])

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
    sketch.write("ARDUINO_DIR = /usr/share/arduino\n"
                    "BOARD_TAG = uno\n"
                    "ARDUINO_PORT = /dev/ttyACM0\n"
                    "ARDUINO_LIBS = grbl\n"
                    "include /usr/share/arduino/Arduino.mk")
    #sketch.write("ARDUINO_DIR = /usr/share/arduino\n")
    #sketch.write("BOARD_TAG = uno\n")
    #sketch.write("ARDUINO_PORT = /dev/ttyACM0\n")
    #sketch.write("ARDUINO_LIBS = grbl\n")
    #sketch.write("include /usr/share/arduino/Arduino.mk\n")
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
    sp.call(["ln", "-s", "/home/pi/bCNC/bCNC", "/home/pi/Desktop/bCNC"])

# Download TeamViewer
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install TeamViewer? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])

# install touchscreen device controller setting utility
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install X utilities? (y/n) ")
if yesno == "y" or debugmode == False:   
    # Install utitilies need for configuring and calibrating X for the piscreen
    # see http://ozzmaker.com/enable-x-windows-on-piscreen/
    sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""", "install", "x11-xserver-utils", "xinput", "evtest", "libtool", "libx11-dev", "autoconf", "libxi-dev", "x11proto-input-dev"])
    #download and install xinput calibrator
    sp.call(["git", "clone", "https://github.com/tias/xinput_calibrator"])
    sp.call(["./autogen.sh"], cwd="xinput_calibrator")
    sp.call(["make"], cwd="xinput_calibrator")
    sp.call(["sudo", "make", "install"], cwd="xinput_calibrator")
    #download and setup the calibration script
    sp.call(["wget", "http://ozzmaker.com/piscreen/xinput_calibrator_pointercal.sh"])
    sp.call(["sudo", "cp", "/home/pi/xinput_calibrator_pointercal.sh", "/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh"])
    sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh"])
    sp.call(["sudo", "sed", "-i", "$ a\sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh", "/home/pi/.config/lxsession/LXDE-pi/autostart"])  #auto load calibration script
    
    # Flip x-axis direction for touchscreen to match flipped display orientation
    # if finger movements result in back-to-front mouse movements, swap around the "1" and "0" at the end of the regex
    # see http://www.circuitbasics.com/raspberry-pi-touchscreen-calibration-screen-rotation/
    sp.call(["sudo", "sed", "-i", "/\. \/etc\/X11\/Xsession/ i\DISPLAY=:0 xinput --set-prop 'ADS7846 Touchscreen' 'Evdev Axis Inversion' 0 1", "/etc/X11/xinit/xinitrc"])  # file
    
    #turn off screenssaver with disable.sh
     sp.call(["sudo", "mv", "/home/pi/rpi_cnc_img/disableblank.sh", "/etc/X11/Xsession.d/"])
    sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/disableblank.sh"])
    ################################ backslashes needed?##########################################################
    sp.call(["sudo", "sed", "-i", "$ a\/etc/X11/Xsession.d/disableblank.sh", "/etc/xdg/lxsession/LXDE-pi/autostart"]) # backslashes needed???
    ################################ backslashes needed?##########################################################
    # set login to GUI autologin
    #auto login
    sp.call(["sudo", "sed", "-i", "s/1:12345:respawn:\/sbin\/getty 115200 tty1/1:2345:respawn:\/bin\/login -f pi tty1 <\/dev\/tty1 >\/dev\/tty1 2>&1/", "/etc/rc.local"])
    #auto startx
    sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sudo startx", "/etc/rc.local"])
    #extra step for Jessie. From http://ozzmaker.com/piscreen-driver-install-instructions-2/
    # EDIT: deleted, as already called in firstbooy.py
    #sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])
