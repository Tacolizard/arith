from drawille import Canvas, line
from colorama import *
from math import sin, radians


init()
c = Canvas()
c.clear()

class plot:

	class point:
		def __init__(self, x1, y1):
			c.set(x1, y1)
			print(c.frame())

	class Line():
		def __init__(self, ix1,iy1,ix2,iy2):
			try:
				m = (iy2-iy1)/(ix2-ix1)
			except:
				print('Vertical line error')
			x = ix1
			y = iy1
			while x < ix2:
				c.set(x / 2, (m*x)*2)	
				x+=.1
				
			print(c.frame())

	
			
			
		
