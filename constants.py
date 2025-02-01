import random

class ScreenConfig:
    WIDTH = 800
    HEIGHT = 800

class ParticleConfig:
    RADIUS = 5
    IMPACT_RADIUS = 20 * RADIUS
    COUNT = 500
    TYPES = 4

class TreeConfig:
    CAPACITY = 1

class GraphicConfig:
    PARTICLE_COLOR_MAP = {
        0: (255, 0, 0),
        1: (0, 255, 0),
        2: (0, 0, 255),
        3: (255, 255, 0),
        4: (255, 0, 255),
        5: (0, 255, 255),
        6: (255, 255, 255),
        7: (150,100,250)
    }

class ForceConfig:
    FORCE = 1
    # MATRIX = [[random.uniform(-1,1) for _ in range(ParticleConfig.TYPES)] for _ in range(ParticleConfig.TYPES)]
    MATRIX = [
        [1, 0.5, 0, 0],
        [-0.25, 1, 0.5, 0],
        [0, -0.25, 1, 0.5],
        [0, 0, -0.25, 1]
    ]
    REPULSION_DISTANCE = 5 * ParticleConfig.RADIUS
    REPULSION_FORCE = -2
