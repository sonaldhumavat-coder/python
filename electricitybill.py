print("welcome to electricity bill calculator ₹₹₹")
unit=float(input("Enter units consumed"))
if  unit>50:
    amount=unit*2.60
    surcharge=25
elif unit <= 100:
    amount=130+(unit-50)*3.60
    surcharge=30
elif unit <= 200:
    amount=130+162.50+(unit-100)*5.26
    surcharge=35
else:
    amount=130+162.50+526+(unit-200)*8.45
    surcharge=30
bill=amount+surcharge
print("The electricity bill is ₹",bill)
