import pygame
from ball import Ball

pygame.init()

background_color = (0, 0, 0)
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Falling Balls")

screen.fill(background_color)
pygame.display.update()

clock = pygame.time.Clock()

gameOver = False

myBalls = []
reference_time = pygame.time.get_ticks()
while gameOver is False:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print(myBalls)
            gameOver = True

    current_time = pygame.time.get_ticks()
    if current_time == reference_time + 1000:
        reference_time = current_time
        myBalls.append(Ball(screen))

    pygame.display.update()



        
