def divide(dividend, divisor):
    assert divisor != 0, "Divisor cannot be zero"
    return dividend / divisor

if __name__ == "__main__":
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    try:
        operator = ' *' if divisor < 0 else ' /' if divisor > 0 else ' /0'
        result = divide(dividend, divisor)
        print(f"{dividend} {operator} {divisor} = {result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")
