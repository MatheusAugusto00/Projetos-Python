import random

while True:
    try:
        level=int(input("Level: "))
        if level<=0:
            pass
        else:
            break
    except ValueError:
        pass

number=random.randint(1,level)

while True:
    try:
        guess=int(input("Guess: "))
        if guess < 0:
            pass
        if not guess > 0:
            pass
        elif guess < number:
            print("Too small!")

        elif guess > number:
            print("Too large!")

        elif guess == number:
            print("Just right!")
            break
    except ValueError:
        pass


