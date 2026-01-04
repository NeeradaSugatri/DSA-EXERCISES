# Start with an empty shopping list
shopping_list = []

while True:
    action = input("What do you want to do? (add/remove/show/quit): ").lower()

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added to the list.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from the list.")
        else:
            print("Item not found in the list.")

    elif action == "show":
        print("Shopping list:", shopping_list)

    elif action == "quit":
        print("Exiting shopping list manager. Bye!")
        break

    else:
        print("Invalid option. Try again.")
