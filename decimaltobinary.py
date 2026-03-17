n = float(input("Enter a number"))
i = int(n)
f = n - i
b = ""

while i > 0:
    b = str(i % 2) + b
    i //= 2

fb = ""
c = 0
while f > 0 and c < 10:
    f *= 2
    fb += str(int(f))
    f -= int(f)
    c += 1

print(b + "." + fb)