#!/usr/bin/python2

import pilite
import time
import random

if __name__ == "__main__":
    p=pilite.PiLite()
    p.all_on()
    time.sleep(0.5)
    p.all_off()
    time.sleep(0.5)
    p.set_fb("000000000000000000000111000011111110011111110111111111111101111111101111011000110011000110000000000000000000000000000000000000")
    time.sleep(0.5)
    for i in range(2):
	for i in range(2):
	    p.scroll_left(1)
	    time.sleep(0.1)
	for i in range(5):
	    p.scroll_right(1)
	    time.sleep(0.1)
	for i in range(3):
	    p.scroll_left(1)
	    time.sleep(0.1)
    p.all_off()
    for i in range(33,126):
	p.display_char(1,1,chr(i))
	p.display_char(8,1,chr(i+1))
	time.sleep(0.1)
    p.all_off()
    time.sleep(0.5)
    p.send_wait("Hello")
    p.send_wait("World")
    for speed in [10, 25, 50, 100]:
	p.set_speed(speed)
	p.send_wait("SPEED "+str(speed))
    #          1   2   3   4   5   6   7   8   9  10  11  12  13  14
    bars=[  [  0, 10, 20, 30, 40, 50, 60, 70, 80, 90,100, 70, 40, 10 ],
	    [ 10, 25, 40, 55, 70, 85,100, 85, 70, 55, 40, 25, 10, 0  ],
	    [100,  0, 85, 15, 70, 30, 55, 45, 40, 60, 25, 75, 10, 90 ]	]
    for g in bars:
	for i,b in enumerate(g):
	    p.set_bar(i,b)
	time.sleep(.5)
    p.all_off()
    vu=[100,100]
    for reps in range(100):
	for i,v in enumerate(vu):
	    if vu[i]>0:
		vu[i]-=5
	    if random.random()>0.8:
		vu[i]=100
	    p.set_vu(i,vu[i])
	time.sleep(0.025)
    p.all_off()
    for x in range(14):
	for y in range(9):
	    p.pixel_on(x,y)
    for reps in range(1000):
	p.pixel_off(random.randint(0,13),random.randint(0,8))
    for reps in range(1000):
	p.toggle_pixel(random.randint(0,13),random.randint(0,8))
    p.all_off()
