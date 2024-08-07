import random


def main():
    level=get_level()
    print(level)
    score=0
    for i in range(10):
        ct=0
        x=generate_integer(level)
        y=generate_integer(level) 
        while True:        
            try:
                guess=int(input(f"{x} + {y} = "))
                if guess == x + y:
                    score += 1
                    break
                elif guess != x + y:
                    raise ValueError
            except ValueError:
                print("EEE")
                ct += 1
            print(ct)
            if ct == 3:
                print(f"{x} + {y} = {x + y}")
                break
    
    print("Score:",score)
          
            

def get_level():
    while True:
        try:
            number=int(input("Level: "))
            while number < 1 or number > 3:
                number=int(input("Level: "))
            return number
        except ValueError:
            pass



def generate_integer(_level):
    if _level == 1:
        return random.randint(0,9)
    elif _level == 2:
        return random.randint(10,99)
    elif _level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
