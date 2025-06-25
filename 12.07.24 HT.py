'''n=int(input())
if n%3==0 and n%5==0:
    print("Divisible by both")
elif n%3==0:
    print("Divisible by 3")
else:
    print("Divisible by 5")'''

x=int(input())
y=int(input())
z=int(input())
bill=x+y+z
print(bill)
if bill>400:
    t=6.75/100
    tax=(t*bill)-1
    bill1=bill-int(tax)
    total1=bill1+tax
    tip=(10/100)*tax
    tip_amount=(tax-tip)+20
    total=bill+tip_amount+tax
print(int(tax))
print(int(tip_amount))
print(int(total))

'''weight=float(input())
height=float(input())
sq=height*height
bmi=(weight/sq)
print(f"{bmi:.1f}")
if bmi<16:
    print("Severe Thinness")
elif 16<=bmi<=17:
    print("Moderate Thinness")
elif 17<=bmi<=18.5:
    print("Mild Thinness")
elif 18.5<=bmi<=25:
    print("Normal")
elif 25<=bmi<=30:
    print("Overweight")
elif 30<=bmi<=35:
    print("Obese Class I")
elif 35<=bmi<=40:
    print("Obese Class II")
elif  bmi>40:
    print("Obese Class III")'''


