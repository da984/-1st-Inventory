import re
inventory = {"prod0":{
    "name": "tecno",
    "stock": 12,
    "price": 20000
    },
             "prod1":{
                 "name": "samsung",
                 
                 "stock": 20,
                 "price": 80000  
             },
             "prod2":{
                 "name": "infinix",
                 "stock": 25,
                 "price": 48000
                 }
             }
user_cart = {} 
while True:
    task = input("what would you like to do: \n 1.Add item \n 2.Remove item \n 3.Checkout \n 4.Exit \n" )
# 1return task
    if task == "1":
        request = input("Enter Product ID:")
        if request in inventory:
            try:
                quantity = int(input("How many do you want: "))
            except ValueError:
                print("Please enter a valid number.")
            else:
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    available = inventory[request]["stock"] - user_cart.get(request, 0)
                    if quantity > available:
                        print("Insufficient quantity")
                    else:
                        user_cart[request] = user_cart.get(request, 0) + quantity
                        print(f"Added {quantity} {inventory[request]['name']} to your cart")
        else:
            print("Product does not4git exist")
            
    elif task == "2":
        request2 = input("What item would you like to remove i.e. prodID: ")

        if request2 in user_cart:
            try:
                quantity2 = int(input("How many items do you want to remove: "))
            except ValueError:
                print("Please enter a valid number.")
            
            else:
                if quantity2 <= 0:
                    print("Quantity must be greater than zero.")
                elif quantity2 > user_cart[request2]:
                    print("Insufficient quantity")
                elif quantity2 == user_cart[request2]:
                    del user_cart[request2]
                    print("Item completely removed from cart")
                else:
                    user_cart[request2] -= quantity2
                    print("Item successfully removed")
        else:
            print("Item not in cart")
                                
    elif task == "3":
        if not user_cart:
            print("Cart is empty")
        else:
            total = 0
            for product_id in user_cart:
                quantity = user_cart[product_id]
                price = inventory[product_id]["price"]
                item_total = quantity * price
                total += item_total
                print(inventory[product_id]["name"], quantity, item_total)
            print("Total:", total)
            validemail = input("Enter your valid email address: ")
            pattern = r"[^@]+@[^@]+\.[^@]+"
            if not re.match(pattern, validemail):
                print("Invalid email address.")
            else:
                print("Valid email")
                active_coupons = {"SAVE10": 0.10,
                                  "SAVE20": 0.20
                }
                coup = input("Enter coupon code: ")
                if coup in active_coupons:
                    discount = active_coupons[coup]
                    total *= (1 - discount)
                    print(f"Coupon applied: {coup} - {int(discount * 100)}% off")
                elif coup:
                    print("Invalid coupon code.")
                print("Final total:", total)
                for product_id, quantity in user_cart.items():
                    inventory[product_id]["stock"] -= quantity
                user_cart.clear()

    elif task == "4":
        print("Thank you for shopping with us")
        break
    else:
        print("Invalid selection. Choose 1, 2, 3, or 4.")
        
    