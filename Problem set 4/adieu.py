#pip install inflect
import inflect
p=inflect.engine()
names=[]
while True:
    try:
        name=input("Name: ").strip().capitalize()
        names.append(name)
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        break