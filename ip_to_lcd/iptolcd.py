#!/usr/bin/python
__author__ = 'Cody Giles'
__license__ = "Creative Commons Attribution-ShareAlike 3.0 Unported License"
__version__ = "1.0"
__maintainer__ = "Cody Giles"
__status__ = "Production"

import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime

def connect_type(word_list):
    """ This function takes a list of words, then, depeding which key word, returns the corresponding
    internet connection type as a string. ie) 'ethernet'.
    """
    if 'wlan0' in word_list or 'wlan1' in word_list:
        con_type = 'wifi'
    elif 'eth0' in word_list:
        con_type = 'ethernet'
    else:
        con_type = 'current'

    return con_type

# Change to your own account information
# Account Information
# to = 'username@email.com' # Email to send to.
# gmail_user = 'username@gmail.com' # Email to send from. (MUST BE GMAIL)
# gmail_password = 'gmailpassword' # Gmail password.
# smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

# smtpserver.ehlo()  # Says 'hello' to the server
# smtpserver.starttls()  # Start TLS encryption
# smtpserver.ehlo()
# smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

arg='ip route list'  # Linux command to retrieve ip addresses.
# Runs 'arg' in a 'hidden terminal'.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.

# Split IP text block into three, and divide the two containing IPs into words.
ip_lines = data[0].splitlines()
split_line_a = ip_lines[1].split()
split_line_b = ip_lines[2].split()

# con_type variables for the message text. ex) 'ethernet', 'wifi', etc.
ip_type_a = connect_type(split_line_a)
ip_type_b = connect_type(split_line_b)

"""Because the text 'src' is always followed by an ip address,
we can use the 'index' function to find 'src' and add one to
get the index position of our ip.
"""
ipaddr_a = split_line_a[split_line_a.index('src')+1]
ipaddr_b = split_line_b[split_line_b.index('src')+1]

# Creates a sentence for each ip address.
# my_ip_a = 'Your %s ip is %s' % (ip_type_a, ipaddr_a)
# my_ip_b = 'Your %s ip is %s' % (ip_type_b, ipaddr_b)

# Creates the text, subject, 'from', and 'to' of the message.
# msg = MIMEText(my_ip_a + "\n" + my_ip_b)
# msg['Subject'] = 'IPs For RaspberryPi on %s' % today.strftime('%b %d %Y')
# msg['From'] = gmail_user
# msg['To'] = to
# Sends the message
# smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
# smtpserver.quit():w

# and now for the LCD bit....
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_16x2.py
#  16x2 LCD Test Script
#
# Author : Matt Hawkins
# Date   : 06/04/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
 
# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND
 
#import
import RPi.GPIO as GPIO
import time
 
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
 
def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
 
  # Initialise display
  lcd_init()
 
  # Send first IP address to the LCD
  lcd_string("ip_type_a",LCD_LINE_1)
  lcd_string("ipaddr_a",LCD_LINE_2)

  time.sleep(20)

  # Send second IP address to the LCD
  lcd_string("ip_type_b",LCD_LINE_1)
  lcd_string("ipaddr_b",LCD_LINE_2)

  time.sleep(20)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line):
  # Send string to display
 
  message = message.ljust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()
