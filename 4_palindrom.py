n = int (input("Enter the number: "))
t = n
r = 0 
while (n>0):
    dig = n % 10 
    r = r * 10 + dig
    n //= 10

if t == r:
    print("yes")

else:
    print("no")