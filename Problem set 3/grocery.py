grocery_list={}
try:
    while True:
        item=input().strip().lower()

        if item in grocery_list:
            grocery_list[item]+=1
        if item not in grocery_list:
            grocery_list[item]=1

except EOFError:
    pass

sorted_grocery=sorted (grocery_list.items(), key=lambda x: x[0])

for item,count in sorted_grocery:
    print(f"{count} {item.upper()}")
