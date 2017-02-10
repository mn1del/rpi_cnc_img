#!/usr/bin/env python
# helphelp.py
# utility helper functions

import re
import shutil
import os
import subprocess

# chginfile() - replaces strFrom with strTo in file strFilePath
# takes simple string input for strFrom
def chginfile(strFilePath, strFrom, strTo):
    "replaces strFrom with strTo in file strFilePath"
    fin = open(strFilePath, "r")  # input file
    fout = open("temp.txt", "w")  # temporary output file
    patt = re.compile(strFrom)  # pattern
    for line in fin:
        newline = patt.sub(strTo, line)  # replace strFrom with strTo
        print(newline)
        fout.write(newline)
    fin.close()
    fin = None
    fout.close()
    fout = None
    shutil.move("temp.txt", strFilePath)  # replace original with temp.txt
    patt = None
    os.remove("temp.txt")


# chginfile() - replaces regexFrom with strTo in file strFilePath
# for example chginfile_re(fp,"\d.\d","1.2")
# regexFrom argument needs to be passed in quotes
# see http://www.rexegg.com/regex-quickstart.html for regex cheatsheet
def chginfile_re(strFilePath, regexFrom, strTo):
    "replaces regexFrom with strTo in file strFilePath"
    fin = open(strFilePath, "r")  # input file
    fout = open("temp.txt", "w")  # temporary output file
    patt = re.compile(regexFrom)  # pattern
    for line in fin:  # loop through each line in fin
        newline = patt.sub(strTo, line)  # replace strFrom with strTo
        print(newline)  # print to console, not necessary
        fout.write(newline)  # write to temporary file fout
    fin.close()
    fin = None
    fout.close()
    fout = None
    shutil.move("temp.txt", strFilePath)  # replace original with temp.txt
    patt = None
    os.remove("temp.txt")

# cmdcall() - takes a string and passes it into subprocess.call()
# effectively mimics entering a command diarectly into the shell
def cmdcall(commandString)
    "calls command ""commandString"", as if entered in the CLI"
    subprocess.call(commandString.split())
