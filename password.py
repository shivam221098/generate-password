import string
import random
import json


def generator():
    length = int(input("Length: "))
    if length < 8:  # for strong password length should be greater than 8
        print("Too small")
        generator()
    password = [random.sample(upper_alpha, length // 4), random.sample(numbers, 2), random.sample(special, 2),
                random.sample(lower_alpha, length - (length // 4) - 4)]
    #print(password)
    #  converting list of characters in string
    my_password = ""
    for i in password:
        my_password += "".join(i)
    #print(my_password)
    my_password = "".join(random.sample(my_password, length))
    print(my_password)
    # saving password to a file
    with open("password.json", "r", encoding="utf-8") as file:
        data = json.loads(file.read())
    account = input("Account: ")
    data[account] = my_password
    with open("password.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data))


upper_alpha = string.ascii_uppercase
lower_alpha = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

generator()
