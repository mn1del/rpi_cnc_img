#!/usr/bin/env python
# grblconfig.py
# overwrites grbl settings in /home/pi/.bCNC
# uses /home/pi/bCNC/bCNC.ini as the default template


srcPath = "/home/pi/bCNC/bCNC.ini"
tgtPath = "/home/pi/.bCNC"
bCNCConfig = [
        "port = /dev/ttyACM0",
        "pendant = 1",
        "openserial = 1",
        "feedmax_x = 3000",
        "feedmax_y = 3000",
        "feedmax_z = 2000",
        "travel_x = 1800",
        "travel_y = 800",
        "travel_z = 300",
        "safe_z = 5",
        "spindlemin = 0",
        "spindlemax = 12000"
        "grbl_1 = 50",
        "grbl_100 = 40",
        "grbl_101 = 40",
        "grbl_102 = 40",
        "grbl_110 = 3000",
        "grbl_111 = 3000",
        "grbl_111 = 3000"
        ]

# copy default settings
default = open(srcPath, "r")  # open default config file
target = open(tgtPath, "w")  # open target config file
# loop through source config copying the "non-intervention" settings
For line in default:
    for setting in bCNCConfig:
        regx = re.match("^\w*=", setting)  # get bCNCConfig setting name
        if re.match(regx.group(), line):  # check if setting already exists in the file
            target.write(setting + "\n")  # ... in which case use it
        else:
            target.write(line)  # ... otherwise go with the default
target.close()
default.close()

# now cycle through user defined setting lists and add any that haven't aready been captured
newSettings = open(tgtPath, "a").read()
newSettings.write("\n[User Defined Settings]\n")  # append any remaining settings
for setting in bCNCConfig:
    regx = re.match("^\w*=", setting)  # get bCNCConfig setting name
    if re.search(regx.group(), newSettings):  # check if setting is already there
        newSettings.write(setting + "\n")  # append any remaining settings
