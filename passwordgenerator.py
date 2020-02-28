import random
import string


def generate_password(level):
    if level == "easy":
        list = []
        numeric = random.randint(0,99999)
        letters = string.ascii_letters
        for x in range(3):
            x = random.choice(letters)
            list.append(x)
        password = str(numeric)+"".join(list)

        return password
    if level == "medium":
        list = []
        numeric = random.randint(0,99999999)
        letters = string.ascii_letters
        for x in range(5):
            x = random.choice(letters)
            list.append(x)
        password = str(numeric)+"".join(list)

        return password
    if level == "hard":
        list = []
        leftlist = []
        numeric = random.randint(0,9999999999)
        letters = string.ascii_letters
        for x in range(6):
            x = random.choice(letters)
            list.append(x)
        for y in range(6):
            y = random.choice(letters)
            leftlist.append(y)
        password = "".join(leftlist) + str(numeric)+"".join(list)

        return password


print(generate_password("easy"))
print(generate_password("medium"))
print(generate_password("hard"))
