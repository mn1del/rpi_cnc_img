#!/usr/bin/env python
# deals with uploading grbl to arduino
# placed in a separate script to secondboot.py because I couldn't figure out how to CD into 
# the right directory within python, so instead I'll do the "cd'ing" in rc.local, and call standalone script***
#*** EDIT: apparently passing cwd="directory" as an argument after the list in subprocess.call() is how to run the subprocess
# from another directory - which would negate the need to "pre-cd" into the right directory in rc.local


import subprocess as sp

debugmode = False

# upload GRBL to Arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upload GRBL to Arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    #sp.call(["sudo", "make"], cwd="")  # test that the sketch compiles
    sp.call(["sudo", "make", "upload"], cwd="/usr/share/arduino/libraries/grbl/examples/GRBLtoArduino")  # upload to arduino

# set call for everyboot.py
# replaces previous call for secondboot.py
#sp.call(["sudo", "sed", "-i", "/cd \/home\/pi/,/^exit 0/{//!d}", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sudo python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"]) #check backslashes
sp.call(["sudo", "sed", "-i", "/^exit 0/ i\sudo startx", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/ i\\/home\/pi\/bCNC", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/ i\chromium-browser --kiosk http://localhost:8080", "/etc/rc.local"])

# reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Reboot? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "shutdown", "-r"])
