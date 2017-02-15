#!/bin/bash
# secondboot.sh

# remove unnecessary packages
sudo DEBIAN_FRONTEND=noninteractive aptitude -y -q -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' remove wolfram-engine penguinspuzzle dillo squeak-vm squeak-plugins-scratch sonic-pi netsurf-gtk netsurf-common

# upgrade packages
sudo DEBIAN_FRONTEND=noninteractive aptitude -y -q -o Dpkg::Options::='--force-confdef' -o Dpkg::Options::='--force-confold' safe-upgrade

# install numerous packages
sudoDEBIAN_FRONTEND=noninteractiveaptitude-y-q-oDpkg::Options::='--force-confdef'-oDpkg::Options::='--force-confold'installzipunzipxrdppippythonpython-tkpython-pmwpython-imagingarduinoarduino-corearduino-mkgcc-avravr-libcavrdudetightvncserverx11-xserver-utils xinput evtest libtool libx11-dev autoconf libxi-dev x11proto-input-dev

# clone bCNC
sudo git clone https://github.com/vlachoudis/bCNC.git
#create Desktop shortcut
ln -s /home/pi/bCNC/bCNC /home/pi/Desktop/bCNC

# clone grbl
sudo git clone https://github.com/Protoneer/GRBL-Arduino-Library.git /usr/share/arduino/libraries/grbl

#Download TeamViewer installer
wget http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb

# create grbl Makefile
# creates in home directory and then moves to target location
# to get around sudo problems with command piping etc
touch Makefile
# append the following lines to newly created Makefile:
cat <<MYLINES>> Makefile
ARDUINO_DIR = /usr/share/arduino
BOARD_TAG = uno
ARDUINO_PORT = /dev/ttyACM*
ARDUINO_LIBS = grbl
include /usr/share/arduino/Arduino.mk
MYLINES
sudo mv Makefile /usr/share/arduino/libraries/grbl/examples/GRBLtoArduino/Makefile
# upload to Arduino
cd /usr/share/arduino/libraries/grbl/examples/GRBLtoArduino
sudo make upload
cd /home/pi

# downoad/install xinput calibrator (for x windows on piscreen)
git clone https://github.com/tias/xinput_calibrator
cd /home/pi/xinput_calibrator
./autogen.sh
make
sudo make install
cd /home/pi
#download/setup the calibration script
wget http://ozzmaker.com/piscreen/xinput_calibrator_pointercal.sh
sudo cp /home/pi/xinput_calibrator_pointercal.sh /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh
sudo chmod +x /etc/X11/Xsession.d/xinput_calibrator_pointercal.sh
sudo sed -i '$ a\
	sudo/bin/sh/etc/X11/Xsession.d/xinput_calibrator_pointercal.sh' /home/pi/.config/lxsession/LXDE-pi/autostart
# flip axis direction on touchscreen to make screen orientation
sudo sed -i "/\. \/etc\/X11\/Xsession/ i\
	DISPLAY=:0 xinput --set-prop 'ADS7846 Touchscreen' 'Evdev Axis Inversion' 0 1" /etc/X11/xinit/xinitrc

#Turn off screensaver
sudo mv /home/pi/rpi_cnc_img/disableblank.sh /etc/X11/Xsession.d/
sudo chmod +x /etc/X11/Xsession.d/disableblank.sh
sudo sed -i '$ a\
	/etc/X11/Xsession.d/disableblank.sh' /etc/xdg/lxsession/LXDE-pi/autostart

# set autologin
sudo sed -i 's/1:12345:respawn:\/sbin\/getty 115200 tty1/1:2345:respawn:\/bin\/login -f pi tty1 <\/dev\/tty1 >\/dev\/tty1 2>&1/' /etc/rc.local
# set autorun everyboot.py
sudo sed -i '/^exit 0/ i\sudo python /home/pi/rpi_cnc_img/everyboot.py' /etc/rc.local &
# set auto startx
sudo sed -i '/^exit 0/ i\sudo startx' /etc/rc.local
#autolaunch bCNC
sudo sed -i '/^exit 0/ i\\/home\/pi\/bCNC' /etc/rc.local
