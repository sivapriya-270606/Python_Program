#loop
for i in range(10):
    print("hello ram")
for i in range(1,11):
    print(i)
for i in range(1,100,3):
    print(i,end=" ")
print()
for i in range(5,0,-1):
    print(i)

num=int(input("enter number"))
total=0
for i in range(1,num+1):
    total=total+i
print(total)

num1=int(input("enter fnumber:"))
num2=int(input("enter snumber:"))
totals=0
for i in range(num1,num2+1):
    if i%2==0:
        totals+=i
print(totals)

num=int(input("enter number:"))
for i in range(1,11):
    print(num," * ",i," = ",num*i)