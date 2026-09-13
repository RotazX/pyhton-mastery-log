
shopping_list = []

while True:
    item = input("What should I buy? ").lower()
    if item == "done":
        print(sorted(shopping_list))
        break
    else:
        shopping_list.append(item)
