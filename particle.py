from random import randint, uniform
import pygame
from constants import *

class Particle:

    def __init__(self, x = None, y = None, id = None):
        self.x = x if x is not None else randint(0, ScreenConfig.WIDTH)
        self.y = y if y is not None else randint(0, ScreenConfig.HEIGHT)
        self.x_velocity = 0
        self.y_velocity = 0
        self.id = id if id is not None else randint(0, ParticleConfig.TYPES-1)

    def calculate_velocity(self, particles):
        x1, y1 = self.x, self.y
        for particle in particles:
            x2, y2 = particle.x, particle.y
            if abs(x2-x1) > ParticleConfig.IMPACT_RADIUS:
                x2 += ScreenConfig.WIDTH if x2 < x1 else -ScreenConfig.WIDTH
            if abs(y2-y1) > ParticleConfig.IMPACT_RADIUS:
                y2 += ScreenConfig.HEIGHT if y2 < y1 else -ScreenConfig.HEIGHT

            distance = max(((x2-x1)**2 + (y2-y1)**2)**0.5, 1)
            force = self.get_force(distance, particle.id)

            x_force = force * (x2 - x1) / distance
            y_force = force * (y2 - y1) / distance

            self.x_velocity += x_force
            self.y_velocity += y_force


    def get_force(self, distance, particle_id):
        force = ForceConfig.MATRIX[self.id][particle_id]
        if distance <= ForceConfig.REPULSION_DISTANCE:
            return ForceConfig.REPULSION_FORCE - (ForceConfig.REPULSION_FORCE * distance / ForceConfig.REPULSION_DISTANCE)
        elif distance < ForceConfig.REPULSION_DISTANCE + (ParticleConfig.IMPACT_RADIUS - ForceConfig.REPULSION_DISTANCE)/2:
            return force * (distance - ForceConfig.REPULSION_DISTANCE) / (ParticleConfig.IMPACT_RADIUS/2 - ForceConfig.REPULSION_DISTANCE)
        else:
            return force - (force * (distance - ForceConfig.REPULSION_DISTANCE) / (ParticleConfig.IMPACT_RADIUS - ForceConfig.REPULSION_DISTANCE))


    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.x = self.x % ScreenConfig.WIDTH
        self.y = self.y % ScreenConfig.HEIGHT
        self.x_velocity = 0
        self.y_velocity = 0



    def show(self, screen):
        pygame.draw.circle(screen, GraphicConfig.PARTICLE_COLOR_MAP[self.id], (self.x, self.y), ParticleConfig.RADIUS)