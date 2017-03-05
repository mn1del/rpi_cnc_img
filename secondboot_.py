#!/usr/bin/env python
# secondboot.py
# call to the script gets placed in /etc/rc.local by firstboot.py
# ... and then removed by this script (so doesn't get called on every boot,
# just the first boot. The idea is to do basic settings in firstboot.py,
# and set the piscreen up, and then the majority of the RPi_cnc setup
# gets done in this script, when (hopefully) the LCD screen will show progress


import subprocess as sp
import os
#import helpy as h


debugmode = False
bootlog = open("/home/pi/bootlog.txt", "a")  # creat log file to track boot script progress

# remove unnecessary packages
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Remove unnecessary packages? (y/n) ")
    if yesno == "y" or debugmode == False:
        log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""","remove", "wolfram-engine", "penguinspuzzle", "dillo", "squeak-vm", "squeak-plugins-scratch", "sonic-pi", "netsurf-gtk", "netsurf-common"])
        bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""","remove", "wolfram-engine", "penguinspuzzle", "dillo", "squeak-vm", "squeak-plugins-scratch", "sonic-pi", "netsurf-gtk", "netsurf-common"])')
        bootlog.write('\n' + str(log))
        bootlog.write('\n')

## install tightvncserver
#if debugmode == False:
#    yesno = "y"
#else:
#    yesno = raw_input("Install tightvncserver? (y/n) ")
#if yesno == "y" or debugmode == False:
#    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::='--force-confdef'", "-o", "Dpkg::Options::=""--force-confold""",  "install","tightvncserver"])
#    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=--force-confdef", "-o", "Dpkg::Options::=""--force-confold""",  "install","tightvncserver"])')
#    bootlog.write('\n' + str(log))
#    bootlog.write('\n')

# upgrade packages
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upgrade packages? (y/n) ")
if yesno == "y" or debugmode == False:
    #sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "safe-upgrade"])
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "safe-upgrade"])  
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "safe-upgrade"])  ')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install zip/unzip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install zip/unzip? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "zip", "unzip"])
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "zip", "unzip"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install xrdp
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install xrdp? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install","xrdp"])
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install","xrdp"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install pip
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pip? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "python-pip"])
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "python-pip"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install pyserial
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install pyserial? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "pip", "install", "pyserial", "--upgrade"])
    bootlog.write('\nsp.call(["sudo", "pip", "install", "pyserial", "--upgrade"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install python
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install python? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "python", "python-tk", "python-pmw", "python-imaging"])
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "python", "python-tk", "python-pmw", "python-imaging"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "arduino", "arduino-core", "arduino-mk"])
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "arduino", "arduino-core", "arduino-mk"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "gcc-avr", "avr-libc", "avrdude"])
    bootlog.write('\nsp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""",  "install", "gcc-avr", "avr-libc", "avrdude"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install GRBL and configure Makefile (which is the mechnism by which it gets uploaded to arduinio
# the actual uploading will be handled by another script because "cd'ing" into the directory is necessary
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Clone GRBL? (y/n) ")
if yesno == "y" or debugmode == False:
    grbldir = "/usr/share/arduino/libraries/grbl"
    log = sp.call(["sudo", "git", "clone", "https://github.com/Protoneer/GRBL-Arduino-Library.git", grbldir])
    bootlog.write('\nsp.call(["sudo", "git", "clone", "https://github.com/Protoneer/GRBL-Arduino-Library.git", grbldir])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    grbldir = grbldir + "/examples/GRBLtoArduino/Makefile"
    log = sp.call(["sudo", "touch", grbldir])
    bootlog.write('\nsp.call(["sudo", "touch", grbldir])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "chmod", "777", grbldir])
    bootlog.write('\nsp.call(["sudo", "chmod", "777", grbldir])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    sketch = open(grbldir,"w")
    sketch.write("ARDUINO_DIR = /usr/share/arduino\n"
                    "BOARD_TAG = uno\n"
                    "ARDUINO_PORT = /dev/ttyACM*\n"
                    "ARDUINO_LIBS = grbl\n"
                    "include /usr/share/arduino/Arduino.mk")
    sketch.close()

# upload GRBL to Arduino
if debugmode == False:
    yesno = "n"
else:
    yesno = raw_input("Upload GRBL to Arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    #sp.call(["sudo", "make"], cwd="")  # test that the sketch compiles
    log = sp.call(["sudo", "make", "upload"], cwd="/usr/share/arduino/libraries/grbl/examples/GRBLtoArduino")  # upload to arduino
    bootlog.write('\nsp.call(["sudo", "make", "upload"], cwd="/usr/share/arduino/libraries/grbl/examples/GRBLtoArduino")  # upload to arduino')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# clone bCNC
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Clone bCNC? (yes/no)")
if yesno == "y" or debugmode == False:
    log = sp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"], cwd="/home/pi")
    bootlog.write('\nsp.call(["sudo", "git", "clone","https://github.com/vlachoudis/bCNC.git"], cwd="/home/pi")')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "chmod", "111", "/home/pi/bCNC/bCNC"])
    bootlog.write('\nsp.call(["sudo", "chmod", "111", "/home/pi/bCNC/bCNC"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# Create bCNC Desktop Shortcut 
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Create bCNC Desktop Shortcut? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["ln", "-s", "/home/pi/bCNC/bCNC", "/home/pi/Desktop/bCNC"])
    bootlog.write('\nsp.call(["ln", "-s", "/home/pi/bCNC/bCNC", "/home/pi/Desktop/bCNC"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# Download TeamViewer
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install TeamViewer? (y/n) ")
if yesno == "y" or debugmode == False:
    log = sp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])
    bootlog.write('\nsp.call(["wget", "http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

# install touchscreen device controller setting utility
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Install X utilities? (y/n) ")
if yesno == "y" or debugmode == False:   
    # Install utitilies need for configuring and calibrating X for the piscreen
    # see http://ozzmaker.com/enable-x-windows-on-piscreen/
    log = sp.call(["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""", "install", "x11-xserver-utils", "xinput", "evtest", "libtool", "libx11-dev", "autoconf", "libxi-dev", "x11proto-input-dev"])
    bootlog.write('["sudo", "DEBIAN_FRONTEND=noninteractive", "aptitude", "-y", "-q", "-o", "Dpkg::Options::=""--force-confdef""", "-o", "Dpkg::Options::=""--force-confold""", "install", "x11-xserver-utils", "xinput", "evtest", "libtool", "libx11-dev", "autoconf", "libxi-dev", "x11proto-input-dev"]')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')

    #download and install xinput calibrator
    log = sp.call(["git", "clone", "https://github.com/tias/xinput_calibrator"])
    bootlog.write('\nsp.call(["git", "clone", "https://github.com/tias/xinput_calibrator"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["./autogen.sh"], cwd="xinput_calibrator")
    bootlog.write('\nsp.call(["./autogen.sh"], cwd="xinput_calibrator")')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["make"], cwd="xinput_calibrator")
    bootlog.write('\nsp.call(["make"], cwd="xinput_calibrator")')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "make", "install"], cwd="xinput_calibrator")
    bootlog.write('\nsp.call(["sudo", "make", "install"], cwd="xinput_calibrator")')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    #download and setup the calibration script
    log = sp.call(["wget", "http://ozzmaker.com/piscreen/xinput_calibrator_pointercal.sh"])
    bootlog.write('\nsp.call(["wget", "http://ozzmaker.com/piscreen/xinput_calibrator_pointercal.sh"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "cp", "/home/pi/xinput_calibrator_pointercal.sh", "/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh"])
    bootlog.write('\nsp.call(["sudo", "cp", "/home/pi/xinput_calibrator_pointercal.sh", "/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh"])
    bootlog.write('\nsp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "sed", "-i", "$ a\sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh", "/home/pi/.config/lxsession/LXDE-pi/autostart"])  #auto load calibration script
    bootlog.write('\nsp.call(["sudo", "sed", "-i", "$ a\sudo /bin/sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh", "/home/pi/.config/lxsession/LXDE-pi/autostart"])  #auto load calibration script')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    
    # Flip x-axis direction for touchscreen to match flipped display orientation
    # if finger movements result in back-to-front mouse movements, swap around the "1" and "0" at the end of the regex
    # see http://www.circuitbasics.com/raspberry-pi-touchscreen-calibration-screen-rotation/
    log = sp.call(["sudo", "sed", "-i", "/.\/etc\/X11\/Xsession/ i\DISPLAY=:0 xinput --set-prop 'ADS7846 Touchscreen' 'Evdev Axis Inversion' 1 0", "/etc/X11/xinit/xinitrc"])  # file
    bootlog.write('\nsp.call(["sudo", "sed", "-i", "/.\/etc\/X11\/Xsession/ i\DISPLAY=:0 xinput --set-prop "'"ADS7846 Touchscreen"'" "'"Evdev Axis Inversion"'" 1 0", "/etc/X11/xinit/xinitrc"])  # file')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    
    #turn off screenssaver with disable.sh
    log = sp.call(["sudo", "mv", "/home/pi/rpi_cnc_img/disableblank.sh", "/etc/X11/Xsession.d/"])
    bootlog.write('\nsp.call(["sudo", "mv", "/home/pi/rpi_cnc_img/disableblank.sh", "/etc/X11/Xsession.d/"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    log = sp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/disableblank.sh"])
    bootlog.write('\nsp.call(["sudo", "chmod", "+x", "/etc/X11/Xsession.d/disableblank.sh"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    ################################ backslashes needed?##########################################################
    log = sp.call(["sudo", "sed", "-i", "$ a\/etc/X11/Xsession.d/disableblank.sh", "/etc/xdg/lxsession/LXDE-pi/autostart"]) # backslashes needed???
    bootlog.write('\nsp.call(["sudo", "sed", "-i", "$ a\/etc/X11/Xsession.d/disableblank.sh", "/etc/xdg/lxsession/LXDE-pi/autostart"]) # backslashes needed???')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    ################################ backslashes needed?##########################################################
    # set login to GUI autologin
    #auto login
    log = sp.call(["sudo", "sed", "-i", "s/1:12345:respawn:\/sbin\/getty 115200 tty1/1:2345:respawn:\/bin\/login -f pi tty1 <\/dev\/tty1 >\/dev\/tty1 2>&1/", "/etc/rc.local"])
    bootlog.write('\nsp.call(["sudo", "sed", "-i", "s/1:12345:respawn:\/sbin\/getty 115200 tty1/1:2345:respawn:\/bin\/login -f pi tty1 <\/dev\/tty1 >\/dev\/tty1 2>&1/", "/etc/rc.local"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    #auto startx
    #extra step for Jessie. From http://ozzmaker.com/piscreen-driver-install-instructions-2/
    log = sp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])
    bootlog.write('\nsp.call(["sudo", "sed", "-i", "s/\/dev\/fb0/\/dev\/fb1/", "/usr/share/X11/xorg.conf.d/99-fbturbo.conf"])')
    bootlog.write('\n' + str(log))
    bootlog.write('\n')
    
# set call for everyboot.py
# replaces previous call for secondboot.py
# everyboot.py will have instructions like startx etc, not rc.local
#sp.call(["sudo", "sed", "-i", "/cd \/home\/pi/,/^exit 0/{//!d}", "/etc/rc.local"])
bootlog.write('\n#sp.call(["sudo", "sed", "-i", "/cd \/home\/pi/,/^exit 0/{//!d}", "/etc/rc.local"])')
bootlog.write('\n' + str(log))
bootlog.write('\n')
#sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sudo python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"]) #check backslashes
log = sp.call(["sudo", "sed", "-i", "1,$ s/secondboot_\.py/everyboot.py/g", "/etc/rc.local"])  # set everyboot.py
bootlog.write('\nsp.call(["sudo", "sed", "-i", "1,$ s/secondboot_\.py/everyboot.py/g", "/etc/rc.local"])  # set everyboot.py')
bootlog.write('\n' + str(log))
bootlog.write('\n')
#sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sudo startx", "/etc/rc.local"])
#sp.call(["sudo", "sed", "-i", "/^exit 0/ i\/home/pi/bCNC", "/etc/rc.local"])
#sp.call(["sudo", "sed", "-i", "/^exit 0/ i\chromium-browser --kiosk http://localhost:8080", "/etc/rc.local"])

bootlog.close()

# reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Reboot? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "shutdown", "-r"])
