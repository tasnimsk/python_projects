import random

print("Your password:")
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?"

password = ""
for x in range(8):
    password += random.choice(chars)

print(password)