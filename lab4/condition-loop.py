def vowel(char):
    return char.lower() in 'aeiou'

def convert_uppercase_vowels(input_string):
    uppercase_vowels = []

    for char in input_string:
        if not vowel(char):
            continue 

        uppercase_vowels.append(char.upper())

    return uppercase_vowels

if __name__ == '__main__':
    user_input = input("Enter a string:")

    result = convert_uppercase_vowels(user_input)
    print(f"Chars are [{', '.join(element for element in user_input)}]")

    if result:
        print(f"The entered string is {user_input} and the result of convert a vowels to uppercase is\n [" + ', '.join(result) + "]")
    else:
        print(f"There are no vowel in the entered string {user_input}")
