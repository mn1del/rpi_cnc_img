# List of VFD settings for Huanyang VFD
# Not really a python file. Just helps with syntax highlighting in VIM.

'''
Unlock settings, and set to factory state to get started
'''
PD000 = 0  # 0 to unlock, 1 to lock
PD013 = 8  # "8" restores factory settings. Start here

'''
Configure power and motor settings
'''
PD005 = 400  # Max operating freq.
PD004 = 400  # Base freq
PD003 = 400  # Main freq (techincally irrelevant when operating from external inputs)
PD006 = 20  # Intermediate freq. Feaul 2.5 when default max freq is 400. Therefore 20 for 400 is right????????
PD008 = 220  # max voltage
PD009 = 15  # Intermediate voltage. 15 corresponds to 220v input
PD010 = 8  # Min voltage. 8 corresponds to 220v input
PD011 = 0  # Lower frequency limit. 0 is ok for water cooled spindle. Must be higher for air cooled.
PD014 = 10  # Accel time 1
PD015 = 10  # Decel time 1
PD016 = 10  # Accel time 2 
PD017 = 10  # Decel time 2
PD018 = 10  # Accel time 3
PD019 = 10  # Decel time 3
PD020 = 10  # Accel time 4
PD021 = 10  # Decel time 4
PD072 = 400  # Max analog external input freq
PD073 = 0  # Min analog external input freq
PD141 = 220  # rated motor voltage
PD142 = 10  # rated motor amps. 2.2kw/220v = 10 amps. Theoretically could set higher because of cable loss
PD143 = 2  # number of poles. 2 for the 2.2kw spindle. Calculate as max RPM = 120 * freq/poles
PD144 = 3000  # Rated motor rpm at 50Hz (24000 @ 400Hz = 3000 @ 50Hz)


'''
Drive from external inputs (not by front panel operator buttons)
nb not sure if pwm spindle control is enabled on my cnc shield. One forum implied that Z+ and Z- was z-limit, butnow is spindle-PWM. And SpnEn was spindle enable and is now z-limit. And SpnDir was spindle direction and is now spindle enable. See : http://blog.protoneer.co.nz/arduino-cnc-shield/
'''
PD001 = 1  # Run commands from external terminal
PD002 = 1  # Operating frequency from external terminal
PD070 = 1  # set analog input to 5V. Compatible with Arduino Uno
PD044 = 2  # i/o [FOR] terminal function set to "forward rotation"  
PD023 = 0  # Disable reverse rotation
PD024 = 1  # enable vfd stop button, even when drive from external terminals
