amount=int(input("Amount to widhtdraw"))
note1=(amount//100)
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("For 100 rs notes",note1,"notes")
print("For 50 rs notes",note2,"notes")
print("For 10 rs notes",note3,"notes")
