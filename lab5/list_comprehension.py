def vowel(char):
    return char.lower() in 'aeiou'


def convert_uppercase_vowels(input_string):
    return [char.upper() for char in input_string if vowel(char)]


if __name__ == '__main__':
    user_input = input("Enter a string:")

    print(f"Chars are [{', '.join(element for element in user_input)}]")

    result = convert_uppercase_vowels(user_input)

    if result:
        print(
            f"The entered string is {user_input} and the result of converting vowels to uppercase is\n[" + ', '.join(result) + "]")
    else:
        print(f"There are no vowels in the entered string {user_input}")
