from drawille import Canvas, line, Turtle, polygon
from colorama import *
from math import sin, radians


init()
c = Canvas()
c.clear()
pnts = []
t = Turtle()
tpos = []


class plot:

	def lnres(inres):
		res = inres
				
	def printc(color):
		for x,y in pnts:
			c.set(x,y)
		if color == 'green':
			print(Fore.GREEN+c.frame())
		if color == 'red':
			print(Fore.RED+c.frame())
		if color == 'yellow':
			print(Fore.YELLOW+c.frame())
		if color == 'blue':
			print(Fore.BLUE+c.frame())
		if color == 'cyan':
			print(Fore.CYAN+c.frame())
		
		
	def printt():
		print(t.frame())
		
	def allclear():
		t.clear()
		c.clear()

	class point:
		def __init__(self, x1, y1):
			c.set(x1, y1)
			print(c.frame())

	class ln():
		def __init__(self, ix1,iy1,ix2,iy2):
			try:
				m = (iy2-iy1)/(ix2-ix1)
			except:
				print('Vertical line error')
			x = ix1
			y = iy1
			while x < ix2:
				pnt = x, (m*x)
				pnts.append(pnt)	
				x+=2
				
	class sine:
		def __init__(self,start,end,res):
			for x in range(start,end,res):
				pnt = x / 10, 10 + sin(radians(x)) * 10
				pnts.append(pnt)
					
	

	
			
			
		
