import os
import random


def main():

    family_file = "Data/family_name.txt"
    lastname_file = "Data/lastname_name.txt"

    # 62
    for i in range(250):
        family_name = open(family_file).read().splitlines()
        lastname_name = open(lastname_file).read().splitlines()
        file_to_generate(random.choice(family_name), random.choice(
            lastname_name))


def file_to_generate(x, y):
    complete_name = str(x) + " " + str(y)
    signs = [".", "_", random.randrange(1, 2001)]
    random_signs = random.choice(signs)
    email = ""
    if random_signs == ".":
        email = str(x)+str(random_signs)+str(y)+str(signs[2])
    elif random_signs == "_":
        email = str(x)+str(random_signs)+str(y)+str(signs[2])
    elif isinstance(random_signs, int):
        email = str(x)+str(y)+str(signs[2])
    complete_email = email.lower() + "@gmail.com"
    phone_number = "07" + str(random.randrange(20, 70)) + \
        str(random.randrange(200000, 999999))

    with open("Data/Final_Trained_Data.txt", "a", encoding='utf-8') as f:
        f.write(complete_email + " / " + complete_name +
                " / " + phone_number + " \n")
        f.close()


if __name__ == "__main__":
    main()
