#pip install pyfiglet
from pyfiglet import Figlet
import sys
import random

figlet=Figlet()
list=figlet.getFonts()


if len(sys.argv) == 1:
    _font=random.choice(list)
    figlet.setFont(font=_font)
    frase=input("Type: ")
    print(figlet.renderText(frase))
elif len(sys.argv) == 3:
    if (sys.argv[1])=="-f" or (sys.argv[1])=="--font":
        figlet.setFont(font=(sys.argv[2]))
        frase=input("Type: ")
        print(figlet.renderText(frase))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Infalid usage")










