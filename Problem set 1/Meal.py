def main():
    x=input("What time is it?: ")
    result=convert(x)
    if(7<=result<9):
        print("breakfast time")
    elif(12<=result<14):
        print("lunch time")
    elif(18<=result<20):
        print("dinner time")


def convert(time):
    hours,minutes=time.split(":")
    hours=float(hours)
    minutes=float(minutes)
    return hours+minutes/60

if __name__ == "__main__":
    main()