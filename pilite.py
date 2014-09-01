#!/usr/bin/python2

"""
This python module provides an interface to the Ciseco Pi-LITE LED matrix
through the Raspberry Pi's serial port.
Before use, you will need to follow the instructions at
http://tinyurl.com/omk9pby to disable the Pi using the serial port for login.

Stephen Blythe 2014
"""

import serial
import sys
import time

class PiLite:
    """Functions to control the PiLite.  Instantiate the class to initialise
    the serial port using, for example:
    pilite=PiLite()
    Then call the other methods using the pilite object.
    """

    BAUDRATE=9600
    TIMEOUT=0
    PORT="/dev/ttyAMA0"
    SPEED=50
    COLS_PER_CHAR=6 #inc. space

    def __init__(self):
	self.s=serial.Serial()
	self.s.baudrate=PiLite.BAUDRATE
	self.s.timeout=PiLite.TIMEOUT
	self.s.port=PiLite.PORT
	try:
	    self.s.open()
	except serial.SerialException, e:
	    sys.stderr.write("could not open port %r: %s\n"%(s.port,e))
	    sys.exit(1)
	self.set_speed(PiLite.SPEED)

    def send(self,text):
	"""Send a string to the PiLite, can be simple text or a $$$ command"""
	#print text
	self.s.write(text)
	time.sleep(0.001*len(text))

    def send_wait(self,text):
	"""Send a string to the PiLite, sleep until the message has been
	displayed (based on an estimate of the speed of the display.
	Due to the font not being monotype, this will wait too long in most
	cases"""
	self.send(text)
	time.sleep(len(text)*PiLite.COLS_PER_CHAR*self.speed/1000.0)

    def send_cmd(self,cmd):
	"""Send a $$$ command - just pass the command itself to this function
	without the $$$ at the beginning or the CR at the end"""
	self.send("$$$"+cmd+"\r")

    def all_on(self):
	"""Switch on all LEDs"""
	self.send_cmd("ALL,ON")

    def all_off(self):
	"""Switch off all LEDs"""
	self.send_cmd("ALL,OFF")

    def set_speed(self,speed):
	"""Set the display speed.  The parameters is the number of milliseconds
	between each column scrolling off the display"""
	self.speed=speed
	self.send_cmd("SPEED"+str(speed))

    def set_fb(self,fb):
	"""Set the "frame buffer".  fb is a string of "1" and "0" for each pixel
	"""
	self.send_cmd("F"+fb)

    def _set_indexed_value(self,cmd,index,value):
	self.send_cmd(cmd+str(index+1)+","+str(value))

    def set_bar(self,index,value):
	"""Assuming a vertical bar graph using each column of the display, set
	column "index" to percentage "value".  Columns are indexed 0-13 from
	left to right"""
	self._set_indexed_value("B",index,value)

    def set_vu(self,index,value):
	"""Assuming a horizontal bar graph with each bar using 5 rows of the
	display, set row "index" to percentage "value".  Rows are indexed 0-1
	from top to bottom"""
	self._set_indexed_value("V",index,value)

    def set_pixel(self,x,y,state):
	"""Set pixel at "x,y" to "state" where state can be one of "ON", "OFF"
	or "TOGGLE"
	"""
	self.send_cmd("P"+str(x+1)+","+str(y+1)+","+state)

    def pixel_on(self,x,y):
	"""Switch on pixel at "x,y"
	"""
	self.set_pixel(x,y,"ON")

    def pixel_off(self,x,y):
	"""Switch off pixel at "x,y"
	"""
	self.set_pixel(x,y,"OFF")

    def toggle_pixel(self,x,y):
	"""Toggle pixel at "x,y"
	"""
	self.set_pixel(x,y,"TOGGLE")

    def scroll(self,value):
	"""Scroll the whole display "value" columns to the left.  Use negative
	values to scroll to the right.
	"""
	self.send_cmd("SCROLL"+str(value))

    def scroll_left(self,value):
	"""Scroll the whole display "value" columns to the left.
	"""
	self.scroll(value)

    def scroll_right(self,value):
	"""Scroll the whole display "value" columns to the right.
	"""
	self.scroll(-value)

    def display_char(self,x,y,char):
	"""Display character "char" with its top left at "x,y"
	"""
	self.send_cmd("T"+str(x+1)+","+str(y+1)+","+char)
