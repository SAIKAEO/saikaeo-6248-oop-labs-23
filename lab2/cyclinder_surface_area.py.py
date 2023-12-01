import math


def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def main():
    while True:
        radius = float(input("Enter radius:"))
        if radius >= 0:
            break
        else:
            print("Please enter a positive number for radius")
            return
    height = float(input("Enter height:"))
    if height < 0:
        print("Please enter a positive number for height")
        return
    surface_area = cylinder_surface_area(radius, height)
    print(
        f"The surface area of a cylinder with radius {radius:.1f} and heigh {height:.2} is {surface_area:.2f}")


if __name__ == "__main__":
    main()
