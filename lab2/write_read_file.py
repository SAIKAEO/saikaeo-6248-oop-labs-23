number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
result = number1 + number2
print(f"{number1} + {number2} = {result:.1f}")

with open('numbers.txt', 'w') as file:
    file.write(f"{number1} + {number2} = {result:.1f}\n")
print("Writing to file numbers.txt")

with open('numbers.txt', 'r') as file:
    file_data = file.read()
print("Reading from file numbers.txt")
print(file_data)

