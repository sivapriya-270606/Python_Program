#match case
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
operator=input("enter operator:")
match operator:
    case '+':print(num1+num2)
    case '-':print(num1-num2)
    case '*':print(num1*num2)
    case '/':print(num1/num2)
    case '//':print(num1//num2)
    case '%':print(num1%num2)
    case '**':print(num1**num2)

file=input("enter the file extension:")
match file:
    case 'py':print("python file")
    case 'c':print("c file")
    case 'c++':print("c++ file")
    case 'html':print("HTML file") 
    case 'jpg':print("image file")
    case '_':print("unknown file")
