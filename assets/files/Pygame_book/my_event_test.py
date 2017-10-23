#/usr/bin/env python
#coding=utf8

import random, pygame, sys
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480

def main():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('event test')


	while True:
		for event in pygame.event.get():
			print 'event.type' , event.type

			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				print event.key 


if __name__ == '__main__':
	main()