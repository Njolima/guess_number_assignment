import random

first_list = list(range(10))
random.shuffle(first_list)
digits = (first_list[:3])
print(digits)
print("WELCOME TO THE GUESS_NUMBER GAME")

entry=input("enter 3-digit number")

