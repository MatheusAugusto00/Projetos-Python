def calculate_fraction():
    while True:
        try:
            x,y=map(int,input("Fraction: ").split("/"))
            (x/y)*100
            if x>y:
                print("Y value must be higher than X")
            else:
                return round((x/y)*100)

        except ValueError:
            print("A fraction must be typed(Ex:1/4)")

        except ZeroDivisionError:
            print("Y value can´t be zero")


def main():
    x=calculate_fraction()
    if x>=99:
        print("F")
    elif x<=1:
        print("E")
    else:
        print(f"{x}%")


main()
