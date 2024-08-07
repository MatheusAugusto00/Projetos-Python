def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def remove_punctuation(s):
    for letter in s:
        if letter in [".","!","/"]:
            return True

def check_string(s):
    for letter in s:
        if letter.isnumeric():
            if s[s.index(letter):len(s)].isnumeric():
                return False
            else:
                return True
def check_zero(s):
    for letter in s:
        if letter.isnumeric():
            if s[s.index(letter):len(s)].startswith("0"):
                return True
            else:
                return False
def is_valid(s):

    if 2>len(s):
        return False
    elif len(s)>6:
        return False
    elif s[0].isdigit():
        return False
    elif s[1].isdigit():
        return False
    elif check_string(s):
        return False
    elif remove_punctuation(s):
        return False
    elif check_zero(s):
        return False
    else:
        return True



main()

