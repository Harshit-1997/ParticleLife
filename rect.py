from constants import *

class Rect:
    def __init__(self,x1 = 0, y1 = 0, x2 = ScreenConfig.WIDTH, y2 = ScreenConfig.HEIGHT):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    
    def contains(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
    

    def intesects_with_circle(self, x, y, r):
        x_dist , y_dist = 0, 0
        if self.x1 <= x <= self.x2:
            x_dist = 0
        elif x < self.x1:
            x_dist = min(self.x1 - x, ScreenConfig.WIDTH - (self.x2 - x))
        else:
            x_dist = min(x - self.x2, ScreenConfig.WIDTH - (x - self.x1))

        if self.y1 <= y <= self.y2:
            y_dist = 0
        elif y < self.y1:
            y_dist = min(self.y1 - y, ScreenConfig.HEIGHT - (self.y2 - y))
        else:
            y_dist = min(y - self.y2, ScreenConfig.HEIGHT - (y - self.y1))

        return x_dist**2 + y_dist**2 <= r**2
    
    
    def quadsect(self):
        '''Return a tuple of four Rects that are the quadrants of this Rect in order of top-left, top-right, bottom-left, bottom-right.'''
        midx = (self.x1 + self.x2) // 2
        midy = (self.y1 + self.y2) // 2
        return (Rect(self.x1, self.y1, midx, midy),
                Rect(midx, self.y1, self.x2, midy),
                Rect(self.x1, midy, midx, self.y2),
                Rect(midx, midy, self.x2, self.y2))