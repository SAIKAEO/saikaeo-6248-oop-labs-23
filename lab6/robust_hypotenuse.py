import math

def compute_hypotenuse(a, b):
    try:
        a = (a)
        b = (b)
        result = math.sqrt(a**2 + b**2)
        return result
    except (ValueError, TypeError):
        return "None"

if __name__ == "__main__":
    print(f"hypotenuse(3.0, 4.0) is {compute_hypotenuse(3.0, 4.0)}")
    print(f"hypotenuse(3, 4)     is {compute_hypotenuse('3', '4')}")
    print(f"hypotenuse(3, 4.0)   is {compute_hypotenuse(3, '4.0')}")
