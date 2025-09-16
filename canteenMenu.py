#canteen menu --->
# project 01 --->
#It shows the menu, lets the user pick something, adds the price, and prints the total ✅

        
        
beverages = ["Tea🍵 - 10 ", "Coffee☕- 15", "Cold Drink🍸 - 30","lemonade- 45"]
snacks = ["Burger 🍔- 50", "Pizza 🍕- 120","Sandwich🥪 - 80","Fries🍟 - 60"]
chips = ["Lays - 20", "Doritos - 35","Uncle Chips - 25"]

beverages_price = [10, 15, 30,45]
snacks_price = [50, 120, 80, 60]
chips_price = [20, 35,25]

total = 0

print("📋 Welcome to the Canteen 😋")
print("1. Beverages🍹")
print("2. Snacks🍟")
print("3. Chips🥫")

choice = int(input("Choose a category (1-3): "))


if choice == 1:
    print("\nBeverages Menu:")
    for i in range(len(beverages)):
        print(f"{i+1}. {beverages[i]}")
    item = int(input("Choose item number: "))
    total += beverages_price[item-1]

elif choice == 2:
    print("\nSnacks Menu:")
    for i in range(len(snacks)):
        print(f"{i+1}. {snacks[i]}")
    item = int(input("Choose item number: "))
    total += snacks_price[item-1]

elif choice == 3:
    print("\nChips Menu:")
    for i in range(len(chips)):
        print(f"{i+1}. {chips[i]}")
    item = int(input("Choose item number: "))
    total += chips_price[item-1]

else:
    print("Invalid choice!")

print(f"\n✅ Final Bill: {total}")



