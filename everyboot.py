#!/usr/bin/env python
# everyboot.py
# place code that should be run on every boot here


import subprocess as sp

# launch GUI
sp.call(["git", "pull"], cwd="/home/pi/rpi_cnc_img")
sp.call(["startx"])
