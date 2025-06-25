#1
balance=5000
while True:
    print("1.Deposit""\n""2.Withdraw""\n""3.View Balance""\n""4.Exit")
    operation=int(input())
    match operation:
        case 1:
            dep=int(input("Enter amount to Deposit:"))
            balance=balance+dep
            print("Money deposited successfully!")
        case 2:
            wit=int(input("Enter amount to withdraw:"))
            balance=balance-wit
            print("Money withdrawal complete")
        case 3:
            print("Account balance is:",balance)
        case 4:
            quit()
        case _:
            print("Invalid Input")

#2
seashell_restaurant={
    "Biriyani":["Mutton Biriyani----Rs.290","Chicken Biriyani----Rs.180","Fish Biriyani----Rs.200","Veg Biriyani----Rs.150"],
    "Dessert":["Ice cream----Rs.100","Falooda----Rs.150","Gulab Jamun----Rs.120"],
    "Starters":["Lollipop----Rs.200","Chilli Chicken----Rs.250","Fish 65----Rs.280"]
    }
while True:
    print("Categories""\n""1.Biriyani""\n""2.Dessert""\n""3.Starters""\n""Press enter to quit")
    user_choice=input("Enter the item which you need:").capitalize()
    if user_choice in seashell_restaurant:
        print(f"{user_choice}->")
        for i in seashell_restaurant[user_choice]:
            print(".",i)
    else:
        quit()
