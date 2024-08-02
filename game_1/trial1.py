import pygame

pygame.init()

LENGTH=800
WIDTH=600

screen =  pygame.display.set_mode((LENGTH, WIDTH))
pygame.display.set_caption('Game')
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    screen.fill('white')
    pygame.display.update()

pygame.quit()