def get_float(arg):
    while True:
        try:
            return float(input(f"Please enter {arg} floating point number:"))
        except ValueError:
            print("Please enter a valid floating point number")


def add():
    num1 = get_float("the first")
    num2 = get_float("the second")

    operator = input("Please enter the operation (+, -, *, /): ")

    if operator in ('+', '-', '*', '/'):
        if operator == '/' and num2 == 0:
            print("Cannot divide by zero.")
            exit()
        else:
            try:
                result = eval(f"{num1} {operator} {num2}")
                print(f"The result of adding {num1} {operator} {num2} = {result}")
            except:
                exit()
    else:
        print("Unknown operator")
        exit()


if __name__ == "__main__":
    add()
