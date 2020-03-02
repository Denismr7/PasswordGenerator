import random
import string
import json


def generate_password(level):
    if level == "easy":
        list = []
        numeric = random.randint(0, 99999)
        letters = string.ascii_letters
        for x in range(3):
            x = random.choice(letters)
            list.append(x)
        generate_password.password = str(numeric) + "".join(list)

        return generate_password.password
    if level == "medium":
        list = []
        numeric = random.randint(0, 99999999)
        letters = string.ascii_letters
        for x in range(5):
            x = random.choice(letters)
            list.append(x)
        generate_password.password = str(numeric) + "".join(list)

        return generate_password.password
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
        generate_password.password = "".join(leftlist) + str(numeric) + "".join(list)

        return generate_password.password


def save():
    save = input("Do you want to save the password? (Yes/No) ")
    if save.lower() == "yes":
        passname = str(input("Type the password's name: "))
        data = list({passname + ": " + str(generate_password.password)})
        print(data)
        with open("passwords.txt", "a") as passwordlist:
            passwordlist.write(json.dumps(data))
            print(f"Password for {passname} saved!")


print("Hi! Welcome to password generator, in order to bring you a safe password, first let us know which security "
      "level do you want your password to have")
while True:
    level = input("Easy, Medium or Hard? ")
    if level.lower() in ("easy", "medium", "hard"):
        if level.lower() == "easy":
            print("Your password is: " + generate_password("easy"))
            save()
        if level.lower() == "medium":
            print("Your password is: " + generate_password("medium"))
            save()
        if level.lower() == "hard":
            print("Your password is: " + generate_password("hard"))
            save()
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
