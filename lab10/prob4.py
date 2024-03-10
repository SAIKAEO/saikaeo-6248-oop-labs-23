import sys

if len(sys.argv) != 4 or any(not arg.isdigit() for arg in sys.argv[2:]):
    print("Usage: python calculator.py <operator> <operand1> <operand2>")
    sys.exit(1)

operator = sys.argv[1]
operator1 = float(sys.argv[2])
operator2 = float(sys.argv[3])

if operator == '+':
    print(f'{operator1} {operator} {operator2} is {operator1 + operator2}')
elif operator == '-':
    print(f'{operator1} {operator} {operator2} is {operator1 - operator2}')
elif operator == 'x':
    print(f'{operator1} {operator} {operator2} is {operator1 * operator2}')
elif operator == '/':
    try:
        print(f'{operator1} {operator} {operator2} is {operator1 / operator2}')
    except ZeroDivisionError:
        print(f'{operator1} cannot be divided by {operator2}')
