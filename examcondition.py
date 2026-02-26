medicalcause=str(input("Is there any medical cause (Yes/no)").strip().upper())
if medicalcause == "NO":
    print("You are allowed for the examination")
else:
    attendence=float(input("Enter your attendence (%)"))
    if attendence > 80:
        print("You are allowed")
    else:
        print("You are not allowed for the examination")



