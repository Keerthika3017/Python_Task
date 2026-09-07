num = int(input("Enter a number: "))
if num > 10:
    print("Positive")
elif num < 10:
    print("Negative")
else:
    print("Zero")

    
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

    
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
        print()


num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")

    
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum:", max(a, b, c))
print("Minimum:", min(a, b, c))

