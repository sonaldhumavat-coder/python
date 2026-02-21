bp=float(input("Please enter buying price"))
sp=float(input("Please enter selling price"))
if sp>bp:
    print("Profit by",sp-bp,"Rupees")
else:
    print("loss by",bp-sp,"rupees")