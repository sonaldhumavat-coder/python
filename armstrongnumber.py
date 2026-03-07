n=int(input("Enter a number"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**4
    temp//=10
if n==sum:
    print("Its a armstrong number")
else:
    print("It is isnt a armstrong number")
  


