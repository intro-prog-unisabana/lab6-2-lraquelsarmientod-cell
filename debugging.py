def show_inventory(inventory):
    print("\nCurrent Inventory:")
    # FIX 1: usar .items() para iterar correctamente
    for fruit, stock in inventory.items():
        print(f"{fruit}: {stock}")
    print()

def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    # FIX 2: no necesitas .keys()
    if fruit in inventory:
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        # FIX 3: usar = en vez de ==
        inventory[fruit] = int(stock)
        print(f"{fruit} added with stock {stock}.\n")

def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    # FIX 4: no usar .items()
    if fruit in inventory:
        amount = input(f"Enter amount to add to {fruit}'s stock: ")
        # FIX 5: convertir a entero antes de sumar
        inventory[fruit] += int(amount)
        print(f"{fruit} stock increased by {amount}.\n")
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.\n")

def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")

def run_program():
    # FIX 6: faltaban comas en el diccionario
    inventory = {
        "apples": 10,
        "bananas": 20,
        "oranges": 15
    }

    # FREEZE CODE BEGIN
    print("Welcome to the Fruit Shop!\n")

    while True:
        menu()
        choice = input("Enter option number: ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_fruit(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")
  
if __name__ == "__main__":
    run_program()
    # FREEZE CODE END