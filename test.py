import pygame
from pygame.locals import *

from quadtree import QuadTree
from random import randint
from constants import *
from particle import Particle

pygame.init()
screen = pygame.display.set_mode((ScreenConfig.WIDTH, ScreenConfig.HEIGHT))
clock = pygame.time.Clock()


def main():
    tree = QuadTree()
    for idx in range(ParticleConfig.COUNT):
        particle = Particle()
        tree.insert(particle.x, particle.y, particle)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.fill((0, 0, 0))
        for particle in tree:
            particle.show(screen)
        

        tree2 = QuadTree()
        for particle in tree:
            neighbors = tree.get_elements_in_circle(particle.x, particle.y, ParticleConfig.IMPACT_RADIUS)
            particle.calculate_velocity(neighbors)
        
        for particle in tree:
            particle.move()
            tree2.insert(particle.x, particle.y, particle)
        tree = tree2
        tree.show(screen)

        pygame.display.flip()
        clock.tick(60)

    
        

if __name__ == '__main__':
    main()

    
