shopping_list = []

while True:
    choice = input("add / remove / show / quit: ").lower()

    if choice == "add":
        item = input("Item name: ")
        shopping_list.append(item)
    elif choice == "remove":
        item = input("Item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found")
    elif choice == "show":
        print(shopping_list)
    elif choice == "quit":
        break
    else:
        print("Invalid option")
