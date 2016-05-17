from lib import *
import os

os.system('clear')

#all plot.ln drawn from 0,0 and infinitely long. they may not render all points however

#lines warp when drawn in non-square terminal

plot.allclear()
#plot.lnres(.05)
plot.ln(0,0,10,0)
plot.ln(0,0,10,5)
plot.ln(5,10,10,5)
plot.sine(0,360,20)
plot.sine(360,720,20)

for x,y in polygon(2,2,9999,20):
	c.set(x,y)
for x,y in polygon(3,3,3,20):
	c.set(x,y)#add to library

plot.printc('blue')
