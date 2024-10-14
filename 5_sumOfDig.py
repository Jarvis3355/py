n = int(input("Enter: "))
t = 0

while n>0:
    dig = n % 10
    t += dig
    n //= 10

print("Total : ",t)