import pygame
from pygame.draw import *
from os import system
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))

circle(screen, (225, 225, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (225, 0, 0), (160, 180), 20)
circle(screen, (225, 0, 0), (240, 180), 15)
circle(screen, (0, 0, 0), (160, 180), 8)
circle(screen, (0, 0, 0), (240, 180), 8)
rect(screen, (0, 0, 0), (160, 250, 100, 15))
polygon(screen, (0, 0, 0), ((290, 130), (225, 180), (215, 175)))
polygon(screen, (0, 0, 0), ((100, 120), (195, 175), (180, 180)))

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
