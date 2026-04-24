import math

class Shape_nbs:
    def area_nbs(self_nbs):
        pass  # Placeholder for polymorphism

class Rectangle_nbs(Shape_nbs):
    def __init__(self_nbs, width_nbs, height_nbs):
        self_nbs.width_nbs = width_nbs
        self_nbs.height_nbs = height_nbs

    def area_nbs(self_nbs):
        return self_nbs.width_nbs * self_nbs.height_nbs

class Circle_nbs(Shape_nbs):
    def __init__(self_nbs, radius_nbs):
        self_nbs.radius_nbs = radius_nbs

    def area_nbs(self_nbs):
        return math.pi * self_nbs.radius_nbs ** 2

class Triangle_nbs(Shape_nbs):
    def __init__(self_nbs, base_nbs, height_nbs):
        self_nbs.base_nbs = base_nbs
        self_nbs.height_nbs = height_nbs

    def area_nbs(self_nbs):
        return 0.5 * self_nbs.base_nbs * self_nbs.height_nbs

# Example usage
rectangle_nbs = Rectangle_nbs(10, 5)
circle_nbs = Circle_nbs(5)
triangle_nbs = Triangle_nbs(8, 6)

print(f"Rectangle Area: {rectangle_nbs.area_nbs()}")
print(f"Circle Area: {circle_nbs.area_nbs():.1f}")
print(f"Triangle Area: {triangle_nbs.area_nbs()}")

#Nicole Sambile