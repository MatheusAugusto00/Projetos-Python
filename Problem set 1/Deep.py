x=input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().title()
if(x=="42"):
    print("Yes")
elif(x=="Forty Two"):
    print("Yes")
elif(x=="Forty-Two"):
    print("yes")
else:
    print("No")