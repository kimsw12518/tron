import pygame
import sys
from pygame.locals import *
from random import *

class player:
        def __init__(self,pl):
        self.x = 0
        self.y = 240+((pl-1.5)*240
        self.dir=5-(2*pl)

pygame.init()
SURFACE=pygame.display.set_mode((600,480))
pygame.display.set_caption("test")
FPSCLOCK=pygame.time.Clock()

def main():
        while True:
                SURFACE.fill((255,255,255))
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                pygame.display.update()
                FPSCLOCK.tick(30)
                                

if __name__=="__main__":
        main()
