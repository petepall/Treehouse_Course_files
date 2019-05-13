sodas = ["Pepsi", "Cherry Coke zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print(f"We're all out of {choice}! Sorry!")
    else:
        print(f"Here's your {choice}: {snack}")
