import random
import pygame

class Ball():

    def __init__(self, surface):
        self.size = 100
        self.color = random.choice([
            (120, 170, 80),
            (70, 50, 30),
            (45, 90, 220)
        ])
        self.draw(surface)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (random.randrange(0, 300), random.randrange(0, 300)), random.randrange(10, 50))
        
