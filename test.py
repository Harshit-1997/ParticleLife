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
    particles = []
    for idx in range(ParticleConfig.COUNT):
        particle = Particle()
        particles.append(particle)
        tree.insert(particle.x, particle.y, idx)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        screen.fill((0, 0, 0))
        for particle in particles:
            particle.show(screen)
        pygame.display.flip()
        clock.tick(60)

        tree2 = QuadTree()
        for idx in tree:
            particle = particles[idx]
            neighbors = [particles[i] for i in tree.get_elements_in_circle(particle.x, particle.y, ParticleConfig.IMPACT_RADIUS)]
            particles[idx].calculate_velocity(neighbors)
        
        for idx, particle in enumerate(particles):
            particle.move()
            tree2.insert(particle.x, particle.y, idx)
        tree = tree2
        # tree.show(screen)

    
        

if __name__ == '__main__':
    main()

    
