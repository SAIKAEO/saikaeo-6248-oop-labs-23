positive_numbers = []

while True:
    number = float(input("Enter a number: "))

    if number <= 0:
        break

    if number.is_integer() and number > 0:
        positive_numbers.append(int(number))

    if not positive_numbers:
        print("No positive integer entered")
    else:
        average = sum(positive_numbers) / len(positive_numbers)
        print("Numbers are:", positive_numbers)
        print("The averages of the positive integers is", average)
