import pygame
import ray_casting
import sys
from ray_calculate import *

WIN_WIDTH = 480
WIN_HEIGHT = 360
 
pygame.init()
 
clock = pygame.time.Clock()
FPS = 60
 
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
def render(distance):
    for a in range(len(distance)):
        shade=50+(distance[a]*(5/8))
        pygame.draw.line(screen, [int(0*shade/100), int(0*shade/100), int(180*shade/100)], [a*5, (-200/distance[a])+WIN_HEIGHT/2], [a*5, (200/distance[a])+WIN_HEIGHT/2], 5)
    
    pygame.display.update()

    return None

x_player=9
y_player=5
FOV=120
POV=0
world_map=[
"11111111111111111111",
"10000000100000001001",
"10000000100000000001",
"10000000100000000001",
"10000000100000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"10000000000000000001",
"11111111111111111111"]
if __name__=="__main__":
    while True:
        screen.fill((255, 255, 255))
        render(ray_casting.raycasting(world_map, FOV, POV, x_player, y_player))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_TAB]:
                x_player += x_ray_calculation(POV-90, 1)
                y_player += y_ray_calculation(POV-90, 1)
                pygame.time.delay(100)
            else:
                POV-=5
            pygame.time.delay(100)
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_TAB]:
                x_player += x_ray_calculation(POV+90, 1)
                y_player += y_ray_calculation(POV+90, 1)
                pygame.time.delay(100)
            else:
                POV+=5
            pygame.time.delay(100)
        if keys[pygame.K_UP]:
            x_player += x_ray_calculation(POV, 1)
            y_player += y_ray_calculation(POV, 1)
            pygame.time.delay(100)
        if keys[pygame.K_DOWN]:
            x_player -= x_ray_calculation(POV, 1)
            y_player -= y_ray_calculation(POV, 1)
            pygame.time.delay(100)
        clock.tick(FPS)
