# Shopping cart manager

shoppinglist = []

print("Hello beautiful people 💗\nWelcome in your wishlist world 😘😉")

num = int(input("Enter the number of items you want to add😜 (add as your heart wanna)\nBestie, numbers only.....😎\n"))
for i in range(1, num + 1):
    item = input(f"Enter item {i}: ")
    shoppinglist.append(item)

print(f"\nYour shopping items🛍️🛒 are here bestie: {shoppinglist}")

print("Choose your vibe ✨")

print("1 - remove items from cart\n2 - Add more items\n3 - proceed & checkout")
answer=int(input())

if (answer==1):
    


    noOfDeleteItems = int(input("\nEnter the number of items you want to remove: "))
    newlist = []
    for i in range(noOfDeleteItems):
        removeItems = input("Please mention the name of item you want to remove: ")
        newlist.append(removeItems)

    print("\nYou want to remove these items, please re-check:")
    print(newlist)
    
       

# Updated items

    wrongItems = []

    for item in newlist:
        if item in shoppinglist:
            shoppinglist.remove(item)   
        else:
            wrongItems.append(item)

    print("\nOOPS ! Below items are wrong\n(we know your soul wants it😁):")
    print(wrongItems)

    print("\nYour updated cart is here love💗:")
    print(shoppinglist)

    print(f"\nThe number of items in your updated cart is: {len(shoppinglist)}\n thank you for visiting💗")

    
elif answer==2:
    print("WE LOVE PEOPLE when they LISTEN TO THEIR DIL💗")
    add=int(input("please bestie , enter the number of items you want to add"))
    for items in range(1,add+1):
        addItems=input("add the new items ") 
        shoppinglist.append(addItems)
        
    print("your cart is updated")
    print(shoppinglist)
    print(f"number of items in your cart {len(shoppinglist)}")
    
    
        
elif answer==3:
    print("following is your items in the cart")
    print(f"{shoppinglist}\nNUM of items in ypur cart {len(shoppinglist)}")
    
    
    
else:
   print("sis.....you choose wrong number!")

