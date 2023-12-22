def find_vowels(input_string):
    vowels = set("aeiouAEIOU")
    vowels_input = [
        input_string for input_string in input_string if input_string in vowels]
    return vowels_input


def main():
    user_input = input("Enter string input:")
    result = find_vowels(user_input)

    if result:
        print(f"Vowels in  {user_input} are {result}")


if __name__ == "__main__":
    main()
