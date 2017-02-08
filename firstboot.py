#!/usr/bin/env python
# firstboot.py
# mostly uses subprocess module to access command line commands
# intended to avoid prolonged PiBakery screen, and potentially help with debugging


import subprocess as sp


debugmode = False  # if True, then requires a user prompt for every action

# Expand Filesystem
yesno = input("Expand Filesystem? (y/n)"
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "raspi-config", "nonint", "do_expand_rootfs"])

# update packages
yesno = input("Update Packages? (y/n)"
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "update"])

# install git
yesno = input("Install Git? (y/n)"
if yesno == "y" or debugmode == False:
    sp.call(["sudo", "aptitude", "install","git","-y"])

