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
    h.cmdcall("sudo make upload")  # upload to arduino

