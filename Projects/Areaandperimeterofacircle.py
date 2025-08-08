class calculation:
    def __init__(self, radius):
        self.radius = float(radius)
        self.area = 3.141592654 * self.radius * self.radius
circle = calculation(10)
print(circle.area)
class calculation:
    def __init__(self, radius):
        self.radius = float(radius)
        self.perimeter = 2 * 3.141592654 * self.radius
circle = calculation(10)
print(circle.perimeter)