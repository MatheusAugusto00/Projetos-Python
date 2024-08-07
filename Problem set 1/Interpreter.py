def calculator(inp):
    x ,y,z = inp.split()
    x=float(x)
    z=float(z)
    if y=="+":
        r=x+z
    elif y=="-":
        r=x-z
    elif y=="*":
        r=x*z
    elif y=="/":
        r=x/z
    return(f"{r:.1f}")

def main():
    operation=input("Expression: ")
    result=calculator(operation)
    print(result)

main()
