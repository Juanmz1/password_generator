#password generator
import random

print(" Welcome to your password generator ")
charater = "ABCDEFGHIJKLMNOPQRSTVUWYZabcdefghijklmnopqrstvuwyz0123456789"
number_len = input(" Amount of password to generate ")
len_pwd = input("Enter length of password")
number_len = int(number_len)
len_pwd = int(len_pwd)
print("\n here are your password")

for pwd in range(number_len):
    passwords = ""
    for i in range(len_pwd):
        passwords += random.choice(charater)
print(passwords)
