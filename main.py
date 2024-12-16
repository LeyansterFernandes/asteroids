import pygame
from pygame.math import Vector2
import sys
import random




class FRUIT:
    def __init__(self):
        # Randomly determine an x and y position
        self.x = random.randint(0,cell_number - 1) # Subtracting 1 to show that we are always on screen ( within boundaries )
        self.y = random.randint(0,cell_number - 1 )
        
        # Store x and y coordinates on a vector
        self.pos = Vector2(self.x,self.y)
        # draw a square
        
    def draw_fruit(self):
        # Create Rectangle ( Scale x and y to match grid size)
        x_pos = self.pos.x * cell_size
        y_pos = self.pos.y * cell_size
        fruit_rect = pygame.Rect(int (x_pos), int (y_pos), cell_size, cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)
        
        # draw the rectangle
        
       
# Initialise All Pygame Modules
pygame.init()
cell_size = 40
cell_number = 20

# Main game loop
screen = pygame.display.set_mode((cell_number * cell_size, cell_size * cell_number))
clock = pygame.time.Clock()
framerate = 60
test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))
x = 100
y = 200
w = 100
h = 100

fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(framerate)

