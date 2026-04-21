def add (a,b):
   return a+b
def sub (a,b):
   return a-b
def multiply (a,b):
   return a*b
def divide(a,b):
   return a/b
print("Welcome to python calculator")
print("Please tell the operation that you want to have been done")
print("addition = 1")
print("Subtraction = 2")
print("Division = 3")
print("Multiplication=4")
choice=int(input("Enter the operation number"))
if choice==1:
   a= int(input("Enter the first number"))
   b=int(input("Enter the second number"))
   result=add(a,b)
   print(result)
elif choice==2:
   a= int(input("Enter the first number"))
   b=int(input("Enter the second number"))
   result=sub(a,b)
   print(result)
elif choice==3:
   a= int(input("Enter the first number"))
   b=int(input("Enter the second number"))
   result=divide(a,b)
   print(result)
elif choice==4:
   a= int(input("Enter the first number"))
   b=int(input("Enter the second number"))
   result=multiply(a,b)
   print(result)
else:
   print('INVALID INPUT !!!!')




