import json

filename = "hobbies.json"
data = {"firstName": "Jane", "lastName": "Doe",
        "hobbies": ["running", "sky diving", "singing"]}

with open(filename, "w") as f:
    json.dump(data, f)


with open(filename, "r") as f:
    read_data = json.load(f)

first_name = read_data['firstName']
last_name = read_data['lastName']
hobbies = ", ".join(read_data['hobbies'])

output = f"{first_name} has hobbies as {hobbies}"
print(output)
