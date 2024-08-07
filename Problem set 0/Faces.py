def convert(string):
    string=string.replace(":(","🙁").replace(":)","🙂")
    return string

def main():
    x=input("Digite algo: ")
    y=convert(x)
    print(y)

main()