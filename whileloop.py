#while loop
n=int(input()) #123
digits=0
total=0
while n!=0:
     rem=n%10
     digits+=1
     total=total+rem
     n=n//10
print("no of digits:",digits)
print("sum of digits:",total)

num=int(input()) #38
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums=sums+rem
        num=num//10
    num=sums
else:
    print(num)

amstorng number
num=int(input())
digits=0
temp=num
temp1=num
while num!=0:
    digits+=1
    num//=10
sums=0
while temp!=0:
    rem=temp%10
    sums=sums+rem**digits
    temp=temp//10
if temp1==sums:
    print("amstrong number")
else:
    print("not amstrong number")
