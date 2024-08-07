def remover(tweet):

    for letter in tweet:
        if letter.lower() == "a":
            tweet=tweet.replace("a","").replace("A","")
        elif letter.lower() == "e":
            tweet=tweet.replace("e","").replace("E","")
        elif letter.lower() == "i":
            tweet=tweet.replace("i","").replace("I","")
        elif letter.lower() == "o":
            tweet=tweet.replace("o","").replace("O","")
        elif letter.lower() == "u":
            tweet=tweet.replace("u","").replace("U","")
    return tweet


y=input("What are you thinking?:")
x=remover(y)
print(x)
