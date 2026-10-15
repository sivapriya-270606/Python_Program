number1=int(input("enter the value:"))
number2=int(input("enter the value:"))
number3=int(input("enter the value:"))
if number1>number2 and number1>number3:
    print("number1 is greater")
elif number2>number1 and number2>number3: 
    print("number2 is greater")
else:
    print("number3 is grater") 

num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2:
    if num1>num3:
        print("num1 is greater")
    else:
        print("num3 is greater")   
else:
    if num2>num3:

#shopping
amount=float(input("enter purchase amount:"))
if amount <0:
    print("invalid amount")
else:
    discount=0.0
    if amount>=5000:
        discount=amount*20/100
    elif amount>=2000 and amount <5000:
        discount=amount*10/100
    print("discount amount:",discount) 
    print("final payable amount:",amount-discount)       
