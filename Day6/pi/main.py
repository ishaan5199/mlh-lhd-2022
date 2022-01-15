digit = int(input("No. of places : "))

pi = [3,"."]

dividend = 110805850
divisor = 78256779

for i in range(digit):
    pi.append(dividend // divisor)
    dividend = (dividend % divisor) * 10

print(f"Value of \u03C0 till {digit} decimal places : ", end = "")
for i in pi:
    print(i, end = "")    