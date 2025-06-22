
def grocery_checkout():
    groceries = {
        "orange": 55,
        "banana": 30,
        "bread": 25,
        "milk": 18,
    }
    
    cart = {}
    total_cost = 0.0

    while True:
        item = input("Add an item (or type 'checkout' to finish): ").lower()
        
        if item == "checkout":
            break
        if item in groceries:
            quantity = input("Enter quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                cart[item] = cart.get(item, 0) + quantity
                total_cost += groceries[item] * quantity
                print("Added", quantity, item + "(s).")
            else:
                print("Enter a valid quantity.")
        else:
            print("Item not found.")

    print("\nFinal Bill:")
    for item, quantity in cart.items():
        subtotal = groceries[item] * quantity
        print(quantity, item + "(s) - ETB", format(subtotal, ".2f"), sep="")
    print("Total cost: ETB", format(total_cost, ".2f"), sep="")

# Run the grocery checkout function
grocery_checkout()