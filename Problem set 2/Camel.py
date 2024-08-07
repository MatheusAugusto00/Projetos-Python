def converter(camelcase):
    snakecase=''
    for letter in camelcase:
        if letter.isupper():
            snakecase += "_" + letter.lower()
        else:
            snakecase += letter
    return snakecase


if __name__=='__main__':
    x=input("camelCase: ")
    y=converter(x)
    print("snake_case",y)