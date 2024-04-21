# Write you random password generator program here!
import random

def generate_pw():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"

    pw_length = int(input("Enter the password length: "))
    
    pw = ""
    for i in range(pw_length):
        char = random.choice(characters)
        pw += char

    print(f"Your password: {pw}")

generate_pw()