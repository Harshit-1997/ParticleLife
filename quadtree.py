import pygame
from random import randint
from rect import Rect
from constants import *

class QuadTree:
    def __init__(self, boundary = Rect(), capacity= TreeConfig.CAPACITY):
        self.boundary = boundary
        self.capacity = capacity
        self.points = dict()
        self.divided = False
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))


    def insert(self, x, y, item):
        '''Insert a point into the QuadTree.'''
        if not self.boundary.contains(x, y):
            return False
        if len(self.points) < self.capacity:
            self.points[(x, y)] = item
            return True
        if not self.divided:
            self.split()
        return (self.top_left.insert(x, y, item) or
                self.top_right.insert(x, y, item) or
                self.bottom_left.insert(x, y, item) or
                self.bottom_right.insert(x, y, item))
    
    def get_elements_in_circle(self, x, y, r):
        '''Return a list of all elements in the QuadTree that are within the circle defined by the center (x, y) and radius r.'''
        elements = []
        if not self.boundary.intesects_with_circle(x, y, r):
            return elements
        for point, item in self.points.items():
            x_dist = min(abs(point[0] - x), ScreenConfig.WIDTH - abs(point[0] - x))
            y_dist = min(abs(point[1] - y), ScreenConfig.HEIGHT - abs(point[1] - y))
            if x_dist**2 + y_dist**2 <= r**2:
                elements.append(item)
        if self.divided:
            elements.extend(self.top_left.get_elements_in_circle(x, y, r))
            elements.extend(self.top_right.get_elements_in_circle(x, y, r))
            elements.extend(self.bottom_left.get_elements_in_circle(x, y, r))
            elements.extend(self.bottom_right.get_elements_in_circle(x, y, r))
        return elements

    def split(self):
        '''Split this QuadTree into four children.'''
        top_left, top_right, bottom_left, bottom_right = self.boundary.quadsect()
        self.top_left = QuadTree(top_left, self.capacity)
        self.top_right = QuadTree(top_right, self.capacity)
        self.bottom_left = QuadTree(bottom_left, self.capacity)
        self.bottom_right = QuadTree(bottom_right, self.capacity)
        self.divided = True

    def show(self, screen):
        '''Draw the QuadTree on the screen.'''
        pygame.draw.rect(screen, self.color, (self.boundary.x1, self.boundary.y1, self.boundary.x2 - self.boundary.x1, self.boundary.y2 - self.boundary.y1), 1)
                
        if self.divided:
            self.top_left.show(screen)
            self.top_right.show(screen)
            self.bottom_left.show(screen)
            self.bottom_right.show(screen)


    def __iter__(self):
        '''Return an iterator over all points in the QuadTree.'''
        for item in self.points.values():
            yield item
        if self.divided:
            yield from self.top_left
            yield from self.top_right
            yield from self.bottom_left
            yield from self.bottom_right