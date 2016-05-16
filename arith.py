#Arith v.0.1
#A simple cli repl for graphing and charting math.

#IMPORTS#####################################################################################
from __future__ import print_function
from drawille import Canvas
from math import sin, radians
from colorama import *
import os
#INITIALIZATION##############################################################################
os.system('clear')

init()

c = Canvas() #init drawille canvas

repl = ['']
special = ['sine', 'out']
print('Enter "help" for help. Use [command] -h for command-specific help')
#COMMAND DEFINE##############################################################################
def out(repl):#compute expression like: 1+4-7*9/4
	if 'out' in repl:#check if it's being used. Why here? idk :P
		if len(repl) > 1:
			try:
				print(Fore.GREEN, eval(repl[1]), Style.RESET_ALL)
			except Exception as es:
				print(Fore.RED, es, Fore.RESET)
		else:
			print(Fore.YELLOW + 'do [out -h] if you need help :)' + Fore.RESET)
	
def sine(func):#display a sine using the awesome drawille library
	default = [0, 360, 10]
	rnge = []
	if 'sine' in repl:
		if len(repl) < 2:#draw a demo sine if no args given
			print(Fore.RESET + Fore.YELLOW + 'No inputs; using defaults...' + Fore.RESET)
			rnge = default
				
		if  len(repl) > 2:
			del repl[0]
			rnge = repl
			
		print(Fore.GREEN)
		for x in range(int(rnge[0]), int(rnge[1]), int(rnge[2])):#compute sine and add to canvas
			c.set(x / 10, 10 + sin(radians(x)) * 10)
		
		print(c.frame() + Style.RESET_ALL)#print canvas
		c.clear()#<--- why did it take so long to realize i needed this
		print('')
#CALL COMMANDS###############################################################################
def spec(func):
	out(func)#just call all of the specials because they handle activation
	sine(func)
#MAIN INPUT##################################################################################
while 'exit' not in repl:#detect exit, like a shell
	repl = input('> ')
	repl = repl.split()#split repl at spaces
	
	if special[0] in repl or special[1] in repl: #inefficient but no real workarounds
		if len(repl) > 0:#						unless I want code that makes no sense
			spec(repl)
#PYTHON INPUT################################################################################
	elif len(repl) > 0:
		try:
			exec(repl[0])#execute python code. i forget why i have this it's almost useless
		except Exception as e:
			print(Fore.RED, e, Fore.RESET)
			pass#random passes everywhere from when I was debugging something and I
			#	thought it might help. Hey, I'm not a python master lol.
#END#########################################################################################
			
			
			
			