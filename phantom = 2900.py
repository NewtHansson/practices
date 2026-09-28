def get_integer(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except EOFError:
            print("\nInput closed. Program ended.")
            exit()

def main():
    weapons = {
        1 : ("Phantom", 2900),
        2 : ("Vandal", 2900),
        3 : ("Operator", 4700)
    }

    print("===VALORANT SUPPLY STATION===")
    print("1 - Phantom : 2900VP")
    print("2 - Vandal : 2900VP")
    print("3 - Operator : 4700VP")

    while True:
        weap_num = get_integer("Which weapon would you like? 1, 2, or 3: ")
        if weap_num in weapons:
            weap_kind, weap_price = weapons[weap_num]
            break
        print("Invalid weapon number. Please choose 1, 2, or 3.")

    MAX_QUANTITY = 100
    while True:
        purchase_num = get_integer(f"How many {weap_kind} do you want? ")
        if 1 <= purchase_num <= MAX_QUANTITY:
            break
        print(f"Quantity must be between 1 and {MAX_QUANTITY}.")

    total_price = weap_price * purchase_num
    while True:
        payment = get_integer("Enter your VP amount: ")
        if payment >= 0:
            break
        print("VP amount cannot be negative.")
    still_need = total_price - payment
    change = payment - total_price

    if payment > total_price :
        print(f"enough VP amount! after purchase, you could have {change} VPs left!")
        print("trade successful, see you again!")
    elif payment == total_price :
        print("you just have exact enough VP amount!")
        print("exact payment! perfect!")
    else:
        print(f"not enough VP amount, you still need {still_need} VPs")
try:
    main()
except KeyboardInterrupt:
    print("\nTransaction cancelled. Goodbye!")