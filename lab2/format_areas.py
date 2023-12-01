import math

def calculate_area(radius):
    height = 2 * radius
    area = 2 * math.pi * radius * (radius + height)
    return area, height

def main():
    print("{:<10} {:<10} {:<20}".format("radius", "height", "surface_area"))
    for radius in range(1, 11):
        area, height = calculate_area(radius)
        print(f"{radius:<10} {height:<10} {area:.2f}")

if __name__ == "__main__":
    main()

