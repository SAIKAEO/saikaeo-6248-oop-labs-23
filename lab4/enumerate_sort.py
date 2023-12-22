def demo_prob4():
    fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
    print(
        f"The fruits are {fruits} \nAfter converting fruits to uppercase letters, fruits are")

    for index, fruit in enumerate(fruits):
        print(f"{index + 1}. {fruit.upper()}")

    sorted_fruits = sorted(fruits)

    print("\nAfter sorting fruits, fruits are")
    print("[" + ", ".join(sorted_fruit.upper()
          for sorted_fruit in sorted_fruits) + "]")


if __name__ == '__main__':
    demo_prob4()
