#1
'''try:
    age=int(input())
    assert age>=18,"Participant must be at least 18 years old"
    assert age<60,"Participant must be no older than 60 years old"

except AssertionError as a:
    print("Registration error:",str(a))
else:
    print("Participant is eligible for registration.")

#2
try:
    n1=int(input())
    n2=int(input())
    n3=n1+n2
    print(n3)
except ValueError as a:
    print(a)'''


#3
class InsufficientFundError(Exception):
    pass
class NegativeWithdrawalError(Exception):
    pass
try:
    amount=int(input())
    balance=1000
    if amount<0:
        raise NegativeWithdrawalError("Amount cannot be negative")
    elif amount>balance :
        raise InsufficientFundError("Insufficient Fund")
except NegativeWithdrawalError as a:
    print(f"Error:{a}")
except InsufficientFundError as e:
    print(f"Error:{e}")
else:
    rem=balance-amount
    print("Withdrawn successfully . Your new balance is:",rem)
