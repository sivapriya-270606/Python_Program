
#prime umber
num=int(input())
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime numbers")
else:
    print("not prime number")

for i in range(1,11):
    if i==6:
         break
    print(i,end=" ")
print() 
for i in range(1,11):
    if i==6:
        continue
    print(i,end=" ")

if True and False:
    pass
else:
     print("javascript") 
  
#nested loop
n=int(input())
a=n-1
b=1
for i in range(1,n*2):
    for j in range(1,a+1):
        print(" ",end=" ")
    for k in range(1,b+1):
        print("*",end=" ")
    print()
    if i>=5:
        a+=1
        b-=2
    else:
        a-=1
        b+=2

n=int(input())
a=n+1
b=n
for i in range(1,n*2):
    for j in range(0,a-1):
        print(" ",end=" ")
    for k in range(1,b+1):
        print("*",end=" ")
    print()
    if i>=5:
        a-=1
        b+=1
    else:
        a+=1
        b-=1