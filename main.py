import pygame
import sys

# Initialise All Pygame Modules
pygame.init()

# Main game loop
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
framerate = 60
test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))
x = 100
y = 200
w = 100
h = 100
test_rect = test_surface.get_rect(center = (200,250))
x_pos = 200
y_pos = 200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    screen.fill((175,215,70))
    pygame.draw.rect(screen,pygame.Color('red'),test_rect)
    screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(framerate)

