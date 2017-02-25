#!/usr/bin/env python
# everyboot.py
# place code that should be run on every boot here


import subprocess as sp

# launch GUI
sp.call(["sudo", "startx"])
