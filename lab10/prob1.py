import random
import string


upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

password = (random.choice(upper_case) + random.choice(lower_case) + random.choice(digits) + random.choice(special_characters)
    + ''.join(random.choice(upper_case + lower_case +digits + special_characters) for _ in range(5))
)

print("Random password is:", password)
