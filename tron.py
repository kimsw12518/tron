import pygame
import sys
from pygame.locals import *
from random import *

map=[]
for i in range(0,300):
    map.append([])
    for j in range(0,240):
        map[i].append(0)

class player:
    def __init__(self,pl):
        self.x = 300
        self.y = 240+((pl-1.5)*360)
        self.dir=5-(2*pl)
        self.p=pl
    def move(self):
        global map
        if map[int(self.x/2)][int(self.y/2)]!=0:
            exit()
        map[int(self.x/2)][int(self.y/2)]=self.p
        if self.dir==1:
            self.y=self.y-2
        elif self.dir==2:
            self.x=self.x-2
        elif self.dir==3:
            self.y=self.y+2
        elif self.dir==0:
            self.x=self.x+2

pygame.init()
SURFACE=pygame.display.set_mode((600,480))
pygame.display.set_caption("test")
FPSCLOCK=pygame.time.Clock()
a=player(1)
b=player(2)

def main():
    while True:
        SURFACE.fill((50,50,60))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    b.dir=(b.dir+1)%4
                if event.key == K_RIGHT:
                    b.dir=(b.dir-1)%4
                if event.key == ord('a'):
                    a.dir=(a.dir+1)%4
                if event.key == ord('d'):
                    a.dir=(a.dir-1)%4
        for i in range(0,300):
            for j in range(0,240):
                if map[i][j]==1:
                    pygame.draw.circle(SURFACE, (225,81,0), [int(i*2),int(j*2)],2)
                elif map[i][j]==2:
                    pygame.draw.circle(SURFACE, (0,110,255), [int(i*2),int(j*2)],2)
        pygame.draw.circle(SURFACE, (225,81,0), [int(a.x),int(a.y)],5)
        pygame.draw.circle(SURFACE, (0,110,255), [int(b.x),int(b.y)],5)
        pygame.display.update()
        a.move()
        b.move()
        FPSCLOCK.tick(30)
                

if __name__=="__main__":
    main()
