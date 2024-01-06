from functools import reduce


def reduce_lambda_sum_positive_odd_numbers(numbers):
    filtered_numbers = filter(lambda x: x > 0 and x % 2 != 0, numbers)
    sum_of_positive_odd_numbers = reduce(
        lambda x, y: x + y, filtered_numbers, 0)

    return sum_of_positive_odd_numbers


user_input = input("Enter numbers in the list:")
input_numbers = list(map(int, user_input.split()))

result = reduce_lambda_sum_positive_odd_numbers(input_numbers)
print(result)
