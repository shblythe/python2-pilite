python2-pilite
==============

Python module interface to Ciseco Pi-LITE LED matrix through serial port

Stephen Blythe 2014

# Description
This python module provides an interface to the Ciseco Pi-LITE LED matrix
through the Raspberry Pi's serial port.

# Preparation
Before use, you MUST follow the instructions at http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi/283-setting-up-my-raspberry-pi
to prevent the Pi from using the serial port for login or console-logging.

# Classes
This module contains a single class, PiLite, which you must instantiate to
initialise the serial port using, for example:
```
import pilite
pilite=pilite.PiLite()
```
Then call the other methods using the `pilite` object.

The file `test.py` shows examples of use.

## A note on co-ordinates
The PiLite has 9 rows each containing 14 LEDs.  In this library I have chosen
to stick to the more usual convention of numbering from 0, rather than Ciseco's
preferred convention of numbering from 1.
So, if you use $$$ commands directly, the rows are numbered 1-9 and the columns
1-14, but if you call the methods provided by this module, they are numbered
0-8 and 0-13 respectively.

## PiLite methods

These methods implement the commands described at http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi/280#Using the Pi-Lite pre-loaded software

### send(text)
Send a string to the PiLite, can be simple text or a $$$ command.

### send_wait(text)
Send a string to the PiLite, sleep until the message has been displayed (based
on an estimate of the speed of the display.  Due to the font not being monotype,
this will wait too long in most cases.

### send_cmd(cmd)
Send a $$$ command - just pass the command itself to this function without the
$$$ at the beginning or the CR at the end

### all_on()
Switch on all LEDs

### all_off()
Switch off all LEDs

### set_speed(speed)
Set the display speed.  The parameter is the number of milliseconds between each
column scrolling off the display.

### set_fb(fb)
Set the "frame buffer".  fb is a string of "1" and "0" for each pixel, starting
with the top row from left to right.

### set_fb_pic(pattern)
Set the "frame buffer".  All whitespace is removed from pattern, plus x/y axes are
transposed in the string, and '.' and '*' may be used in place of '0' and '1'.
This allows more "friendly" multi-line string pictures to be passed.

### set_fb_random()
Sets the "frame buffer" to a random pattern of pixels.

### set_bar(index,value)
Assuming a vertical bar graph using each column of the display, set column
"index" to percentage "value".  Columns are indexed 0-13 from left to right

### set_vu(index,value)
Assuming a horizontal bar graph with each bar using 5 rows of the display, set
row "index" to percentage "value".  Rows are indexed 0-1 from top to bottom.

### set_pixel(x,y,state)
Set pixel at "x,y" to "state" where state can be one of "ON", "OFF" or "TOGGLE".

### pixel_on(x,y)
Switch on pixel at "x,y"

### pixel_off(x,y)
Switch off pixel at "x,y"

### toggle_pixel(x,y)
Toggle pixel at "x,y"

### scroll(value)
Scroll the whole display "value" columns to the left.  Use negative values to
scroll to the right.

### scroll_left(value)
Scroll the whole display "value" columns to the left.

### scroll_right(value)
Scroll the whole display "value" columns to the right.

### display_char(x,y,char)
Display character "char" with its top left at "x,y"

