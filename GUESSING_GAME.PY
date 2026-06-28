
import random

secret = random.randint(1, 100)
count = 0



while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("please enter a valid nmber!")
        continue
    
    count = count + 1
    if guess == secret:
        print("correct! you got it in", count, " guesses!")
        break
    elif guess < secret:
        print("too low!")
    else:
        print("too high!")
