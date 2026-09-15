num=int(input("Enter a value:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")


numbers=[33,4,8,56,10]
for i in range(3):
    n=int(input("enter a value:"))
    numbers.append(n)
    print("largest number is",max(numbers))
    
a=int(input("enter a first value:"))
b=int(input("enter a second value:"))
c=int(input("enter a third value:"))
if a>=b and a>=c:
    print("largest:",a)
elif b>=a and b>=c:
    print("largest:",b)
else:
    print("largest:",c)
    
num=int(input("enter a value:"))
for i in range(1,12):
    print(num,"X",i,"=",num*i)


year=int(input("enter a value:"))
if year % 4==0 and year % 100!=0:
    print("leap year")
else:
    print("not leap year")


Mark=int(input("enter a value:"))
if Mark >=40:
    print("Pass")
else:
    print("Fail")
    

for i in range(1,21):
    if i % 3==0:
        continue
    print(i,end="")
    

for num in range(1,51):
 if num%2==0:
    print(num)
    



 
    


    
            
    


    
