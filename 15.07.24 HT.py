#1
cosmetic_brand={
    "Lakme":["Foundation","Matte finish lipstick","Eyeliner"],
    "Maybelline":["Pot kajal","Liner","Lipliner"],
    "Nyka":["Eye shadow","Blush","Mascara"],
    "Myglamm":["Lipstick","Face primer","Compact powder"],
    "L'oreal":["Concealer","Setting spray","Highlighter"]
    }
name=input("Enter the brand you need:").capitalize()
if name in cosmetic_brand:
    print(f"List of {name} products") # List of Myglamm products
    for i in cosmetic_brand[name]:
        print("->",i)
else:
    print("Brand are not available here")
print("~"*20)

#2
calc="1.Add""\n""2.Sub""\n""3.Mul""\n""4.Div""\n""5.Exp"
print(calc)
num1=int(input())
num2=int(input())
operation=int(input())
match operation:
    case 1:
        add=num1+num2
        print("Sum=",add)
    case 2:
        sub=num1-num2
        print("Sub=",sub)
    case 3:
        mul=num1*num2
        print("Multiplication=",mul)
    case 4:
        div=num1/num2
        print("Div=",div)
    case 5:
        exp=num1**num2
        print("Exp=",exp)
    case _:
        print("Invalid input")
