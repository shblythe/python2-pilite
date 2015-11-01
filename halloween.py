#!/usr/bin/python2

import pilite
import time
import random

if __name__ == "__main__":
    p=pilite.PiLite()
    while True:
	p.all_off()
	time.sleep(0.5)
	for _ in range(15):
	    p.set_fb_random()
	    time.sleep(random.random()/10.0)
	    p.all_off()
	    time.sleep(random.random()/10.0)

	p.set_fb_pic("""
	.......*......
	.......*......
	......***.....
	......***.....
	.....*****....
	....*******...
	.*************
	....*******...
	....*********.

	""")
	time.sleep(1)
	for _ in range(5):
	    p.set_fb_pic("""
	    .....****.....
	    ...********...
	    ...********...
	    ....*.**.*....
	    ....******....
	    .....****.....
	    ..............
	    .....****.....
	    ..............
	    """)
	    time.sleep(0.5)
	    p.set_fb_pic("""
	    .....****.....
	    ...********...
	    ...********...
	    ....*.**.*....
	    ....******....
	    .....****.....
	    ..............
	    ..............
	    .....****.....
	    """)
	    time.sleep(0.5)
	for _ in range(4):
	    p.set_fb_pic("""
	    ....*******...
	    ...*********..
	    ...*...*...*..
	    ...*.*.*.*.*..
	    ...*...*...*..
	    ...*********..
	    ...*********..
	    ...*********..
	    ...*.*.*.*.*..
	    """)
	    time.sleep(0.5)
	    p.set_fb_pic("""
	    ....*******...
	    ...*********..
	    ...*...*...*..
	    ...*..**..**..
	    ...*...*...*..
	    ...*********..
	    ...*********..
	    ...*********..
	    ...*.*.*.*.*..
	    """)
	    time.sleep(0.5)
	    p.set_fb_pic("""
	    ....*******...
	    ...*********..
	    ...*...*...*..
	    ...*.*.*.*.*..
	    ...*...*...*..
	    ...*********..
	    ...*********..
	    ...*********..
	    ...*.*.*.*.*..
	    """)
	    time.sleep(0.5)
	    p.set_fb_pic("""
	    ....*******...
	    ...*********..
	    ...*...*...*..
	    ...**..**..*..
	    ...*...*...*..
	    ...*********..
	    ...*********..
	    ...*********..
	    ...*.*.*.*.*..
	    """)
	    time.sleep(0.5)
	p.set_fb_pic("""
	....*******...
	...*********..
	..**..***..**.
	..***********.
	..***********.
	..**.......**.
	..**.*.*.*.**.
	...*********..
	....*******...
	""")
	time.sleep(0.5)
	for i in range(4):
	    for i in range(2):
		p.scroll_left(1)
		time.sleep(0.1)
	    for i in range(3):
		p.scroll_right(1)
		time.sleep(0.1)
	    for i in range(1):
		p.scroll_left(1)
		time.sleep(0.1)
	p.all_off()
	time.sleep(0.5)
	p.set_speed(25)
	p.send_wait("Enter")
	time.sleep(0.5)
	p.send_wait("If")
	time.sleep(0.5)
	p.send_wait("You")
	time.sleep(0.5)
	p.send_wait("Dare!")
	time.sleep(0.5)
	p.all_on()
	for reps in range(200):
	    p.toggle_pixel(random.randint(0,13),random.randint(0,8))
	p.all_off()
