def get_valid_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                print("You can only enter a non-negative integer")
            else:
                return user_input
        except ValueError:
            print("Please enter a valid integer")
        finally:
            print("Stay healthy!")

yesterday_value = get_valid_integer(
    "Enter the number of new infected Covid19 cases for yesterday:")
today_value = get_valid_integer(
    "Enter the number of new infected Covid19 cases for today:")
total_cases = yesterday_value + today_value
percentage_difference = (
    (today_value - yesterday_value) / yesterday_value) * 100
print(f"The difference of the number of new infected cases is {percentage_difference:.2f}%")
