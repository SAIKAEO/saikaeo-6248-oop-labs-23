def find_pattern(text, pattern):
    index = text.find(pattern)
    if index != -1:
        print(f"Found {pattern} in {text} at {index}")
    else:
        print(f"Cannot find {pattern} in {text}")

def main():
    text = input("Enter text:")
    pattern = input("Enter pattern:")
    find_pattern(text, pattern)

if __name__ == "__main__":
    main()
