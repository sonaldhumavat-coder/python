vehical=int(input("Enter your ride (1.two wheeler)(2.car)"))
if vehical==1:
  answer =int(input("bike(1.),scoter(2.)"))
  if answer==1:
    print("You have chose a bike") 
  else:
    print("You have chose a scooter")
elif vehical==2:
  answer =int(input("suv(1.),sedan(2.)"))
  if answer==1:
    print("You have chose a suv") 
  else:
     print("You have chose a sedan")
else:
  print("Invalid input")



