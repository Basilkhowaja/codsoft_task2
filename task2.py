a=int(input("enter the first number"))
b=int(input("enter the second number"))
operation=input("enter the operation you need to perform, choose: +,-,% or x")

if operation=="+" or operation=="add":
    result=a+b 
elif operation=="-" or operation=="subtract":
    result=a-b
elif operation=="%" or operation=="division":
    result=a/b
elif operation=="x" or operation=="multiply":
    result=a*b


print("the result is:",result)
