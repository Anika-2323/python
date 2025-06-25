'''#1 temperature conversion
print("Enter c to convert celsius to fahrenheit")
print("Enter f to convert fahrenheit to celsius")
choice=input("Enter your choice:")
if choice=='c':
    celsius=float(input("Enter temperature in celsius:"))
    fahrenheit=(celsius*9/5)+32
    print("%.2f Celsius: %0.2f Fahrenheit"%(celsius,fahrenheit))
elif choice=='f':
    fahrenheit=float(input("Enter temperature in fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print("%.2f Fahrenheit: %0.2f Celsius"%(fahrenheit,celsius))
else:
    print("Invalid input")

#2 student mark
a=int(input("Enter mark1:"))
b=int(input("Enter mark2:"))
c=int(input("Enter mark3:"))
d=int(input("Enter mark4:"))
e=int(input("Enter mark5:"))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=80:
    print("Grade A")
elif per>=70:
    print("Grade B")
elif per>=60:
    print("Grade C")
elif per>=40:
    print("Grade D")
else:
    print("Grade E")

#3 find the area of rectangle,square,triangle and circle
#area of Rectangle
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
area_rec=l*b
print(f"the area of rectangle is: {area_rec}")
print()
#area of Square
s=int(input("enter the side of the square:"))
area_sq=s*s
print(f"the area of the square: {area_sq}")
print()
#area of triangle
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle: "))
area_tri=1/2*b*h
print(f"the area of the triangle: {area_tri}")
print()
#area of circle
pi=3.14
r=int(input("Enter the radius of the circle:"))
area_cir=pi*r*r
print(f"the area of the circle: {area_cir}")
print()

#4 fibo
n=int(input("enter a number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print(a)

#5 factorial
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a num:"))
print(f"Factorial of {num} is {factorial(num)}")

#6 even odd count array
n=int(input("Enter the number of elements in array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element:")))
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    if i%2!=0:
        odd+=1
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")

#7 upper lower
string=input("enter string:")
lower=0
upper=0
for i in string:
    if i.islower():
        lower+=1
    if i.isupper():
        upper+=1
print("Lower case letters:",lower)
print("Upper case letters:",upper)'''

#8 palindrome

