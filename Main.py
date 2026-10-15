

#list 
# list_1=[24,56,78,9,0,23,23]
# list_2=["akshaya","dharshini","sophia","sivapriya"]
# list_3=["akshaya",20,"A",8.19,"RGCET",True]
# print(list_1)
# print(list_2)
# print(list_3)
# print(type(list_1))
# list_4=[10,20,30,40]
# list_4[2]=300
# print(list_4)

# numbers=[]
# n=int(input())
# for i in range(n):
#     data=int(input())
#     numbers.append((data))
#     print(numbers)

#     list_5=[1,2,3,4,5]
#     print(list_5)
#     for data in list_5:
#         print(data,end=" ")
#     print()
#     i=0 #1<5
#     while i<len(list_5):
#         print(list_5[i],end=" ")
#         i+=1
#     print()
#     list_6=[1,2,3,4,5]
#     list_6.append(6)
#     list_6.append(7)
#     print(list_6)
#     list_6.instert(0,1000)
#     print(list_6)

#     list_7=[10,20,30,40,20,30]
#     list_7.remove(30)
#     print(list_7)
#     list_7.pop()
#     print(list_7)
#     list_7.clear()
#     print(list_7)
#     print("index")
#     list_7=[10,20,30,40,20,30]
#     print(list_7[4])
#     print(list_7[-4])

#     #list slicing
#     nums=[10,20,30,40,50,60] #list[start:stop:step]
#     print(nums[1:4])
#     print(nums[:3])
#     print(nums[3:])
#     print(nums[::2])
#     print(nums[-3:])
#     print(nums[::-1])
#     print(nums[:])

#     nums_1=[10,30,40,10]
#     print(10 in nums_1)
#     print(nums_1.count(10))
#     print(nums_1.index(30))

#     nums_2=[32,78,12,0,-9]
#     nums_2.sort()
#     print(nums_2)
#     nums_2.sort(reverse=True)
#     print(nums_2)

#     nums_3=[4,3,2,1]
#     nums_3.reverse()
#     print(nums_3)

#     nums_4=[56,78,2,3,6,9,4,5,1,2,90,45,23,78,90,345,788,12]
#     print(len(nums_4))
#     print(sum(nums_4))
#     print(min(nums_4))
#     print(max(nums_4))

#two sum
# nums=[]
# n=int(input())
# for i in range(n):
#     data=int(input())
#     nums.append(data)
# target=int(input())
# found=False
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==target:
#             print(f"{i},{j}")
#             found=True
#             break
#     if found:
#         break
# if not found:
#     print("-1,-1")






#strings
name="Rahul"
dept='python'
# a="python" #1000      
# print()
# text="java programming"
# print(text.upper())
# print(text.lower())
# print(text.())
# print(text.count('a'))
# print(text.find("programming"))
# print(text.find("c"))
# print(text.startswith("java"))
# print(text.endswith("programming"))

# text1="         java programming          "
# print(text1.strip())
# text2="java python nodejs"
# courses=text2.split()
# print(courses)

# text3=["python","java","c++"]
# text4=",".join(text3)
# print(text4)


# #functions
# def greet():#function def
#     print("hi jagan")
# greet()
# greet()

# def addition(a,b):
#     print(a+b)

#     addition(5,6)
#     addition(100,200)
#     addition(200,300)

#     def multiplication(a,b,c):
#         return a*b*c
#     result=multiplication(5,5,5)
#     print(result)

#     #global variable and local variable
#     def collage():
#         text="message" #local variable
#         print(text)
#     collage()
#     message="hello" #global variable
#     def google():
#         print(message)
#     google()
        
#recursion
# def greet(n):
#     if n==0:
#         return
#     print("hello jagan")
#     greet(n-1)
# greet(5)

# def counts(num):
#     if num==11: 
#        return
#     print(num,end=" ")
#     counts(num+1)
# counts(1)
# print()
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# n=int(input())
# result=factorial(n)
# print(result)
# a=0
# b=1
# print(a,"",b,end=" ")
# for i in range(3,11):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
# print()
# def fib(num):
#     if num==0 or num==1:
#         return num
#     return fib(num-1)+fib(num-2)

# num=int(input())
# print(fib(num))      
#lambda function
#lambda arguments:expression
# import math
# from math import sqrt
# import Calculator
# addition=lambda a,b:a+b
# print(addition(4,3))
# square=lambda a:a*a
# print(square(5))

# #modules and package
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.pi)

# print(Calculator.multi(5,5,5))

# #exception handling
# try:
#     a=int(input())
#     b=int(input())
#     c=a//b
#     print(c)
# except ZeroDivisionError:
#     print("please enter postive number")
# except ValueError:
#     print("enter integer only")
# finally:
#     print("java programming")

class studenttwo:
    name="unkown"
    mark=0
    def display(self):
        print(self.name," ",self.mark)

class studentone:
    name="naveen" 
    age=20
    dept="cse"
    def marks(self):
        print("maths:90,english:78")

class studentthree:
    name="unknown"
    mark=0
   
    def _init_(self,name,mark):


# class device:
#     def power_on(self):
#         print("device switched on")
# class phone (device):
#     def call(self):
#         print("making a phone call")
# samsung=phone()
# samsung.power_on()
# samsung.call()
# print()
# #multilevel inheritance
# class device:
#     def power_on(self):
#         print("device switched on")
# class computer(device):
#     def run_progam(self):
#         print("running a python program")
# class laptop(computer):
#     def charge(self):
#         print("laptop battery charging")
# asus=laptop()
# asus.power_on()
# asus.run_program(self)
# asus.charge()
# print()
# #multiple inheritance
# class camera:
#     def take_photo(self):
#         print("taking a photo")
# class musicplayer:
#     def play_music(self):
#         print("playing music")
# class smartphone(camera,musicplayer):
#     def call(self):
#         print("making a phone call")
# mi=smartphone
# mi.call()
# mi.power_on()
# mi.take_photo()
# mi.playing music()

#inherarchical inheritance
# class device:
#     def power_on(self):
#         print("device switched on")
# class phone(device):
#     def call(self):
#         print("making a phone call")
# class computer(device):
#     def run_program(self):
#         print("running a python program")
# samsung=phone()
# samsung.call()
# samsung.power_on()
# hp=computer()
# hp.power_on()
# hp.run_program()

#polymorphism
#method overriding
# class phone:
#     def camera(self):
#         print("taking a normal photo")
# class smartphone(phone):
#     def camera(self):
#         print("taking a portrait photo")
# samsung=smartphone()
# samsung.camera()
# nokia=phone()
# nokia.camera()
#encapsulation
# class bank:
#     __amount=800
#     def printamount(self):
#         return self.__amount
# hdfc=bank()
# print(hdfc.printamount)
# #abstraction
# #feature
# from abc import abc,abstractmethod
# class payment(abc):
#     @abstractmethod 
#     def pay(self):
#         pass
# class UPI (payment):
#     def pay(self):
#         print("payment done using upi")
# class phonepe(payment):
#     def pay(self):
#         print("payment done using phonepe")
# payment=UPI()
# payment.pay()
# payment=phonepe
# payment.pay