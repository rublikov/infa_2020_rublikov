import pygame
from pygame.draw import *
from os import system
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 230, 240))
red=[255, 0, 0]
yellow=[255, 255, 0]
blue=[0, 170, 255]
dgreen=[22, 94, 10]
white=[200, 255, 255]
brown=(125, 0, 0)
black=(0, 0, 0)
rect(screen, (30, 210, 0), (0, 200, 400, 200))
def house(x, y, wallcolor, windowcolor, roofcolor, xsize, ysize):
    rect(screen, wallcolor, (x, y, xsize, ysize))
    rect(screen, windowcolor, (x+xsize*0.35, y+ysize*0.35, xsize*0.3, ysize*0.3))
    polygon(screen, roofcolor, ((x, y), (x+xsize*0.5, y-ysize*0.5), (x+xsize, y)))
def tree(x, y, trunkcolor, leavescolor, xs, ys):
    rect(screen, trunkcolor, (x, y, xs, ys))
    circle(screen, leavescolor, (x+xs*1.4, y), xs*1.1)
    circle(screen, leavescolor, (x-xs*0.4, y), xs*1.1)
    circle(screen, leavescolor, (x-xs*0.3, y-xs*1.2), xs*1.1)
    circle(screen, leavescolor, (x+xs*1.3, y-xs*1.2), xs*1.1)
    circle(screen, leavescolor, (x+xs*0.5, y-xs*2), xs*1.1)
def cloud(x, y, cloudcolor, r):
    circle(screen, cloudcolor, (x, y), r)
    circle(screen, cloudcolor, (x+r*0.8, y-r), r)
    circle(screen, cloudcolor, (x+1.6*r, y), r)
    circle(screen, cloudcolor, (x+2.4*r, y-r), r)
    circle(screen, cloudcolor, (x+3.2*r, y), r)
def sun(x, y, r, suncolor):
    polygon(screen, suncolor, ((x-r*0.951, y-r*0.31), (x+r*0.951, y-r*0.31), (x-r*0.587, y+r*0.81), (x, y-r), (x+r*0.587, y+r*0.81)))
    polygon(screen, suncolor, ((x+r*0.951, y+r*0.31), (x-r*0.951, y+r*0.31), (x+r*0.587, y-r*0.81), (x, y+r), (x-r*0.587, y-r*0.81)))
    circle(screen, suncolor, (x, y), r*0.7)
house(25, 225, brown, blue, red, 100, 100)
house(280, 210, brown, blue, red, 60, 60)
tree(150, 225, black, dgreen, 15, 80)
tree(250, 210, black, dgreen, 9, 50)
sun(150, 40, 30, yellow)
cloud(45, 60, white, 20)
cloud(250, 50, white, 16)
cloud(150, 110, white, 18)

            
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        system('cls')
        print(f'x = {pygame.mouse.get_pos()[0]}')
        print(f'y = {pygame.mouse.get_pos()[1]}')
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
