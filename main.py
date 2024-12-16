import pygame
import sys

pygame.init()

#Main game loop
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
framerate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
    clock.tick(framerate)

