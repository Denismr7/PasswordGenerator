import random
import string


def generate_password(level):
    if level == "easy":
        list = []
        numeric = random.randint(0, 99999)
        letters = string.ascii_letters
        for x in range(3):
            x = random.choice(letters)
            list.append(x)
        password = str(numeric) + "".join(list)

        return password
    if level == "medium":
        list = []
        numeric = random.randint(0, 99999999)
        letters = string.ascii_letters
        for x in range(5):
            x = random.choice(letters)
            list.append(x)
        password = str(numeric) + "".join(list)

        return password
    if level == "hard":
        list = []
        leftlist = []
        numeric = random.randint(0, 9999999999)
        letters = string.ascii_letters
        for x in range(6):
            x = random.choice(letters)
            list.append(x)
        for y in range(6):
            y = random.choice(letters)
            leftlist.append(y)
        password = "".join(leftlist) + str(numeric) + "".join(list)

        return password


print("Hi! Welcome to password generator, in order to bring you a safe password, first let us know which security "
      "level do you want your password to have")
while True:
    level = input("Easy, Medium or Hard? ")
    if level.lower() == "easy":
        print("Your password is: " + generate_password("easy"))
    if level.lower() == "medium":
        print("Your password is: " + generate_password("medium"))
    if level.lower() == "hard":
        print("Your password is: " + generate_password("hard"))
    else:
        print("Invalid input")

    answer = input("Do you want to generate another password? (Yes/No) ")
    if answer.lower() == "yes":
        continue
    if answer.lower() == "no":
        print("Ok! Thanks for using us!")
        break
    else:
        break
