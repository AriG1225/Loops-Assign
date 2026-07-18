def showMenu () :
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Done")

def price (choice) :
    if choice == 1:
        return 5.00
    elif choice == 2:
        return 4.00
    elif choice == 3:
        return 6.00
    elif choice == 4:
        return 3.00
    else:
        return 0

def main () :
    orderTotal = 0
    orderList = []
    #welcome message
    print("Welcome to Taco Palace!  Please view the menu below and make a selection")
    #loop
    ordering = True
    while ordering :
        showMenu()
        choice = int(input("Enter your choice: "))
        if choice >= 1 and choice <= 4 :
            if choice == 1:
                itemName = "Taco"
            if choice == 2:
                itemName = "Burrito"
            if choice == 3:
                itemName = "Nachos"
            if choice == 4:
                itemName = "Soft Drink"

            print("Your order: ", itemName)
            orderTotal = orderTotal + price(choice)
            orderList.append(itemName)
        elif choice == 5:
            ordering = False
        else:
            print("Please enter a valid choice")
    print("Thank you for your order!")
    print("Your order is:")
    if len(orderList) > 0:
        for item in orderList:
            print(item)
        else:
            print("Nothing ordered")
    print("Total amount due : $", orderTotal)

main()


