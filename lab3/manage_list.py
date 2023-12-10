# manage_list.py

my_list = [1, 2, 3, 4, 5]


def add_number_to_list():
    global my_list
    user_number = int(input("Enter a number to add to a list:"))
    my_list.append(user_number)
    print(f"After adding an integer {user_number}, the list is {my_list}")
    print("Finding a number to replace in the list", my_list)


def replace_number_in_list():
    global my_list
    if not my_list:
        print("The list is empty. Cannot replace a number.")
        return

    old_number = int(input("Enter a number to find:"))
    new_number = int(input("Enter a number to replace:"))

    try:
        index = my_list.index(old_number)
        my_list[index] = new_number
        print(
            f"After replacing {old_number} with {new_number}, the new list is {my_list}")
    except ValueError:
        print(
            f"Number {old_number} not found in the list. No replacement performed.")


def remove_number_from_list(number_to_remove):
    global my_list
    if not my_list:
        print("The list is empty. Cannot remove a number.")
        return

    try:
        my_list.remove(number_to_remove)
        print(f"After removing {number_to_remove}, the list is {my_list}")
    except ValueError:
        print(
            f"Number {number_to_remove} not found in the list. No removal performed.")


def main():
    new_list = [1, 2, 3, 4, 5, 7]
    print("Before adding an integer, the list is", my_list)

    add_number_to_list()

    replace_number_in_list()

    print("Finding a number to remove in the list", new_list)

    number_to_remove = int(input("Enter a number to remove: "))
    remove_number_from_list(number_to_remove)


if __name__ == "__main__":
    main()
