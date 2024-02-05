import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = math.pi * math.pow(self.radius, 2)
        return area

    def compute_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter


def get_valid_radius():
    while True:
        try:
            radius = float(input("Enter the radius:"))
            if radius >= 0:
                return radius
            else:
                print("Please enter a non-negative value for the radius.")
        except ValueError:
            print("Please enter a valid decimal number")


if __name__ == "__main__":
    radius = get_valid_radius()
    circle = Circle(radius)
    area = circle.compute_area()
    perimeter = circle.compute_perimeter()
    print(
        f"The circle with redius {radius} has thr area as {area:.2f} and the perimeter as {perimeter:.2f} ")
