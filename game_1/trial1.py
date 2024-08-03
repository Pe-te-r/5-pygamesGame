import pygame
import random
import math

pygame.init()

LENGTH=1200
WIDTH=800

screen =  pygame.display.set_mode((LENGTH, WIDTH))
pygame.display.set_caption('Game')
time= pygame.time.Clock()

# player
player = pygame.image.load('assets/images/player.png').convert_alpha()
player_rect = player.get_frect(center=(LENGTH//2,WIDTH//2))

#stars 
stars = pygame.image.load('assets/images/star.png').convert_alpha()
star_positions = [(random.randint(0, LENGTH), random.randint(0, WIDTH)) for _ in range(20)]

#metor
metor = pygame.image.load('assets/images/meteor.png').convert_alpha()
metor_rect =metor.get_frect()

#laser
laser = pygame.image.load('assets/images/laser.png').convert_alpha()
laser_rect = laser.get_rect(bottomleft =(LENGTH-20,WIDTH-20))
running= True
while running:
    time.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    screen.fill('grey')
    for pos in star_positions:
        screen.blit(stars, pos)
    screen.blit(metor,metor_rect)
    screen.blit(laser,laser_rect)
    screen.blit(player,player_rect)
    angle = 0.1
    player_rect.right += math.sin(angle)+1
    player_rect.top -=math.cos(angle)+2
    # player_rect.center = (x,y)
    # player_rect.left -= math.sin(angle)+1
    pygame.display.update()

pygame.quit()