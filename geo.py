class rectangle():
    #define your methods
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length * self.width
    def rectangle_perimeter(self):
        return ((2 * self.length) + (2 * self.length))
    pass
newRectangle = rectangle(18, 20)
print(newRectangle.rectangle_area())
