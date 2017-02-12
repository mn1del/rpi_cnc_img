#!/usr/bin/env python
# deals with uploading grbl to arduino
# placed in a separate script to secondboot.py because I couldn't figure out how to CD into 
# th righ directory within python, so instead I'll do the "cd'ing" in rc.local, and call standalone script


import subprocess as sp

debugmode = False

# upload GRBL to Arduino
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Upload GRBL to Arduino? (y/n) ")
if yesno == "y" or debugmode == False:
    #h.cmdcall("sudo make")  # test that the sketch compiles
    sp.call(["sudo", "make", "upload"])  # upload to arduino

# set call for everyboot.py
# replaces previous call for secondboot.py
sp.call(["sudo", "sed", "-i", "/cd \/home\/pi/,/^exit 0/{//!d}", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \python /home/pi/rpi_cnc_img/everyboot.py", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \sudo startx", "/etc/rc.local"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \\/home\/pi\/bCNC\/bCNC"])
sp.call(["sudo", "sed", "-i", "/^exit 0/i \chromium-browser --kiosk http://localhost:8080", "/etc/rc.local"])

# reboot
if debugmode == False:
    yesno = "y"
else:
    yesno = raw_input("Reboot? (y/n) ")
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "shutdown", "-r"])
