fruit_calories = {"Apple":130,"Avocado":50,"Banana":110,"Cantaloupe":50,"Grapefruit":60,
                  "Grapes":90,"Honeydew melon":50,"Kiwifruit":90,"Lemon":15,"Lime":20,
                  "Nectarine":60,"Orange":80,"Peach":60,"Pear":100,"Pineapple":50,"Plums":70,
                  "Strawberries":50,"Sweet cherries":100,"Tangerine":50,"Watermelon":80}

fruit=input("Item: ").capitalize()

if fruit in fruit_calories:
    print(fruit_calories[fruit])
