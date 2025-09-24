def display_menu():
	print("shopping List Manager")
	print("1.Add Item")
	print("2.Remove Item")
	print("3.View List")
	print("4.Exit")

def add_item():
	item = input("Enter the item to add: ").strip()
	if item:
		shopping_list.append(item)
		print(f"'{item}' has been added to the shopping list.")
	else:
		print("item name cannot be empty.")

def remove_item():
	item = input("Enter item to remove").strip()
	if item in shopping_list:
		shopping_list.remove(item)
		print(f"'{item}'has been removed from the shopping list.")

def view_list():
	if not shopping_list:
		print("your shopping list is empty.")
	else:
        	print("\nYour Shopping List:")	
	for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added.")
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()

