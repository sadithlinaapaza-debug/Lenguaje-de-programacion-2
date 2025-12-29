class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otra):
        return self.x + otra.x, self.y + otra.y

    def __sub__(self, otra):
        return self.x - otra.x, self.y - otra.y

    def __mul__(self, escalar):
        return self.x * escalar, self.y * escalar

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector2D(2, 3)
v2 = Vector2D(1, 1)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
