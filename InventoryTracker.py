inventory = {}

def display_menu():
    print("\nInventory Tracker")
    print("1. Add Item")
    print("2. Update Item Details")
    print("3. Remove Item")
    print("4. View Inventory")
    print("5. Calculate Total Value")
    print("6. Exit")

def add_item():
    item_name = input("Enter item name: ")
    if item_name in inventory:
        print(f"{item_name} already exists. Use 'Update Item Details' to modify it.")
    else:
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
            price = float(input(f"Enter price per unit for {item_name}: "))
            inventory[item_name] = {"quantity": quantity, "price": price}
            print(f"{item_name} added to inventory.")
        except ValueError:
            print("Invalid input. Quantity must be an integer and price must be a number.")

def update_item():
    item_name = input("Enter item name to update: ")
    if item_name in inventory:
        try:
            quantity = int(input(f"Enter new quantity for {item_name} (current: {inventory[item_name]['quantity']}): "))
            price = float(input(f"Enter new price per unit for {item_name} (current: {inventory[item_name]['price']}): "))
            inventory[item_name] = {"quantity": quantity, "price": price}
            print(f"{item_name} updated.")
        except ValueError:
            print("Invalid input. Quantity must be an integer and price must be a number.")
    else:
        print(f"{item_name} not found in inventory.")

def remove_item():
    item_name = input("Enter item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print(f"{item_name} not found in inventory.")

def view_inventory():
    if inventory:
        print("\nCurrent Inventory:")
        print(f"{'Item':<15}{'Quantity':<10}{'Price/Unit':<12}{'Total Value':<12}")
        print("-" * 50)
        for item, details in inventory.items():
            total_value = details["quantity"] * details["price"]
            print(f"{item:<15}{details['quantity']:<10}{details['price']:<12.2f}{total_value:<12.2f}")
    else:
        print("\nInventory is empty.")

def calculate_total_value():
    total_value = sum(details["quantity"] * details["price"] for details in inventory.values())
    print(f"\nTotal inventory value: ${total_value:.2f}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            calculate_total_value()
        elif choice == '6':
            print("Exiting Inventory Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
