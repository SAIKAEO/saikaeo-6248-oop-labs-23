def main():
    original_filename = input("Enter the original filename to read: ")
    new_filename = input("Enter the new filename to write: ")
    text_to_append = input("Enter the text to append: ")

    with open(original_filename, 'r') as f:
        text = f.read()
        print(text)

    # Now you have the content of the original file stored in the 'text' variable
    # You can use this 'text' variable for further processing or writing to another file.

if __name__ == "__main__":
    main()
