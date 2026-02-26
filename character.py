print("welcome to character checker")

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    print("The character is an alphabet.")
else:
    print("The character is NOT an alphabet.")