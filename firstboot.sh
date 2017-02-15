#!/bin/bash
# firstboot.sh
# pure shell version of firstboot script

# enable uploading to arduino
sudo usermod -a -G dialout pi

# enable piscreen driver
sudo sed -i '$ a\dtoverlay=piscreen,speed=16000000,rotate=270' /boot/config.txt
# boot to CLI
# backup:
cp /boot/cmdline.txt /home/pi/cmdline.txt
# settings:
sudo sed -i '1 s/$/  fbcon=map:10 fbcon=rotate:2 fbcon=font:ProFont6x11/' /boot/cmdline.txt

# output display to tft (not hdmi)
sudo sed -i 's/\/dev\/fb0/\/dev\/fb1/' /usr/share/X11/xorg.conf.d/99-fbturbo.conf

# set call for secondboot.py on startup
sudo sed -i '/^exit 0/ i\sleep 10;python /home/pi/rpi_cnc_img/secondboot.py' /etc/rc.local

# reboot
sudo shutdown -r
