# Chatbot's name is Chad
# starter code ->
print("Hi! I'm Chad! I am a chatbot that will help you!")
name = input("what is your name?")
print(f"Hi {name}!")
items = (f"{name},How can I help you today? Select an option by entering the corresponding number on the menu:")

while True:  # ← LOOP STARTS HERE
    # Menu
    print("\n1) Exchange my item with an item from the store. \n2) Return my item to the store \n")
    menu_input = input("Select an option by entering the corresponding number on the menu (or type 'quit' to exit): ")

    if menu_input.lower() == "quit":
        print("Thank you for using Chad the chatbot! Goodbye!")
        break  # stops the loop

    # if-statement ->
    if menu_input == "1": # Exchange
        # what will happen for option 1
        print("You chose to exchange your item.")
        # Ask for item names
        item_name = input("What is the name of the item that you would like to exchange?")
        second_item = input("What is the name of the item you would like to recieve?")
        # Ask for item prices
        item_price = float(input(f"Enter the price of the {item_name}: "))
        s_item_price = float(input(f"Enter the price of the {second_item}: "))
        # Compare prices
        if item_price == s_item_price: # prices match
            print("Great! The prices match. You can exchange the item with no extra cost.")
            print("Here is your reciept:")

            #receipt

            print("\n===== RECEIPT =====")
            print(f"Your item: {item_name} - ${item_price}")
            print(f"Store item: {second_item} - ${s_item_price}")
            print("Price difference: $0.00")
            print("Outcome: Even exchange completed.")
            print("========================\n")
            print("Please send this receipt in the store portal so that a store agent can carry out your transaction")

        elif item_price < s_item_price: # item_price < s_item_price
            difference = round(s_item_price - item_price, 2)
            print(f"The store item is more expensive. You need to pay an additional ${difference}.")
            print("Here is your receipt:")

            # receipt
            print("\n===== RECEIPT =====")
            print(f"Your item: {item_name} - ${item_price}")
            print(f"Store item: {second_item} - ${s_item_price}")
            print(f"Amount owed: ${difference}")
            print("Outcome: Additional payment required.")
            print("========================\n")
            print("Please send this receipt in the store portal so that a store agent can carry out your transaction")


        else:  # item_price > s_item_price
            difference = round(item_price - s_item_price, 2)
            print(f"Your item is more expensive. You will receive ${difference} back.")
            print("Here is your receipt:")

            # receipt

            print("\n===== RECEIPT =====")
            print(f"Your item: {item_name} - ${item_price}")
            print(f"Store item: {second_item} - ${s_item_price}")
            print(f"Amount returned: ${difference}")
            print("Outcome: Refund issued.")
            print("========================\n")
            print("Please send this receipt in the store portal so that a store agent can carry out your transaction")

    elif menu_input == "2": # Return
        # what will happen for option 2
        print("You chose to return your item.")
        # Ask for item name
        item_name = input("What is the name of the item that you would like to exchange?")
        # Ask for item price
        item_price = float(input(f"Enter the price of the {item_name}: "))
        print("Here is your receipt:")

        # receipt

        print("\n===== RECEIPT =====")
        print(f"Returned item: {item_name}")
        print(f"Refund amount: ${round(item_price, 2)}")
        print("Outcome: Item successfully returned.")
        print("========================\n")
        print("Please send this receipt in the store portal so that a store agent can carry out your transaction")

    else: # Invalid input
        # Handles any invalid input
        print("Oops! That is not a valid option. Please enter 1 or 2.")