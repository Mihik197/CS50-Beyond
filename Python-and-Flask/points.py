class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def shift(self, x, y):
        self.x += x
        self.y += y

p = Point(5, 6)
p.shift(3, 4)
print(p.x)