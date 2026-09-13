import random as r

num = r.randint(1, 100)

while True:
    guess = int(input("Guess a random number: "))
    if guess < num:
        print("Too low. Try again!")
    elif guess > num:
        print("Too high. Try again!")
    else:
        print("Correct!!!")
        break