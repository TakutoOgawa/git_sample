class circle:
    def __init__(self, x, y, r):
        self.x, self.y, self.r = x, y, r
        return
    
    def __add__(self, other):
        x = (self.x + other.x) // 2
        y = (self.y + other.y) // 2
        r = max(self.r, other.r)
        return circle(x, y, r)
