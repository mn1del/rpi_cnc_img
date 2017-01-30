# rpi_cnc_img
Create a non-intervention, plug and play RPi image for controlling an RPi driven cnc machine.

Initial ideas:

1) Need an image writer. Options are:
  Pi Bakery
  http://plugwash.raspbian.org/build-image
  http://blog.kmp.or.at/2012/05/build-your-own-raspberry-pi-image/
  https://github.com/andrius/build-raspbian-image
  https://github.com/b-s101/build-raspberrypi-image

2) Method to easily get the RPi's IP address:
  16x2 LCD display?
  small TFT LCD touchscreen display?
  manual search on main computer, using arp -a etc?
  audio blast from RPi on first startup?

3) Things to install/enable:
  Latest Raspbian
  bCNC
    ...and dependancies:
    pySerial
    kTinker
    etc...
  or other GCode streamers: GRBLWeb? UGS? Chillipepper?
  TeamViewer -https://www.youtube.com/watch?v=vr3Gf8vnKAg https://pages.teamviewer.com/published/raspberrypi/
  SSH
  VNC? - http://www.makeuseof.com/tag/run-remote-desktop-raspberry-pi-vnc/
  Xming?
  Camera?
  LCD drivers (if using LCD) - https://github.com/swkim01/waveshare-dtoverlays
  XDRP (for Windows remote Desktop), RDP (windows) or RC Client for Mac/iOS (https://itunes.apple.com/us/app/microsoft-remote-desktop/id714464092?mt=8)
  
4) Settings to update:
  RPi hostname (?)
  RPi p'wrd
  Wifi/ethernet setup
  TeamViewer setup - need to get id, method of generating p'word, or use static? Also possibility of changing framebuffer resolution 
  VNC at boot: http://www.makeuseof.com/tag/run-remote-desktop-raspberry-pi-vnc/
  Static IP address... change the dynamic one to static one
  
5) CNC gui/interface
  Default to headless use, or try and fit on LCD?
  Use direct bCNC input?
  Or use thin layer on top, accessing bCNC commads using shell scripts?
    would require some minimal feedback options: spindle position, hitting stops, tool changes etc etc
  Push CAM file to bCNC from main Computer? Pull CAM file from RPi?
    definitely needs some kind of human interface at the machine. Can be v simple - "GO" button, or can be more involved - interface for downloading the file. Depends on whether LCD display is setup or not.
  Need some kind of homing procedure.
    
  
  
