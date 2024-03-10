import re


def extract_name_and_id(info_str):
    pattern = r"My name:\s*(.*?)\s*My ID is (\d+)"
    matches = re.findall(pattern, info_str)
    if matches:
        for match in matches:
            name = match[0]
            ID = match[1]
            print("My name is", name)
            print("My ID is", ID)
    else:
        print("Name and/or ID not found in the string.")


if __name__ == "__main__":
    my_info = "My name: Manee DeeJai My ID is 642285829"
    extract_name_and_id(my_info)
