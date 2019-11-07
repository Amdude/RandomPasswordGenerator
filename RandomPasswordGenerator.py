from random import randint
import string

all_characters = []  # set up this array to hold our letters and special characters
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']  # array of special characters
password = []  # our array that will be used to store out password


def combine_chars():
    for char in string.ascii_letters:  # add all characters in ascii_letters to all_characters array
        all_characters.append(char)
    for char in special_characters:  # add all characters in special_characters to all_characters array
        all_characters.append(char)


def greeting():
    print("\nHello. Welcome to the random password generator!")
    choose_length()


def choose_length():
    password_length = int(input("How long do you want your password to be?"))  # get password length
    print("Your password will be " + str(password_length) + " characters long.")
    generate_password(password_length)  # create a random password, passing our desired length


def generate_password(length):
    current_length = 0

    while current_length <= length:  # while the current_length of our password is <= to desired password_length
        rand_char = randint(0, len(all_characters) - 1)  # select a random number
        password.append(all_characters[rand_char])  # use that random number to access a character by index
        current_length += 1  # increment current_length by 1

    present_password()


def present_password():
    print("\nHere is your password:")
    print(''.join(password))


combine_chars()
greeting()
