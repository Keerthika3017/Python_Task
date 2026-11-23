'''
#Arithmetic operators
#Addition
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a+b)

#Subtraction
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a-b)

#Devision
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a/b)

#Multiplication
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a*b)

#Floor division
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a//b)

#remainder
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a%b)

#square
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a**b)

#average
T=int(input("tamil mark:"))
E=int(input("english mark:"))
M=int(input("maths mark:"))
SCI=int(input("science mark:"))
S=int(input("social mark:"))
total=T+E+M+SCI+S
a=total/5
print("total:",T+E+M+SCI+S)
print("Average:",a)

#last 2 digit
a=121793
b=a%100
print("last two digit:",b)

#remove last 3 digit
a=157390
b=a//1000
print("last three digit:",b)

#Assignment operators
#name
a="Keerthi"
print(a)

#operators
a=100
a+=50
print(a)
a-=20
print(a)
a*=5
print(a)
a/=2
print(a)
a%=3
print(a)
a**=5
print(a)

#comparision operator
#equal
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a==b)

#not equal
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a!=b)

#biggest
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a>b)

#voting
a=int(input("enter age:"))
if a>=18:
    print("eligible for votting")
else:
    print("not eligible")

#pass
a=int(input("enter a mark:"))
if a>=35:
    print("Passed")
else:
    print("Failed")

#check
a=int(input("enter a num:"))
if 1<=100:
    print("checked")
else:
    print("not found")

#Logical operator
a=6
print(a>0 and a%2==0)

#voting
a=int(input("enter a:"))
print(a>0 and a>=18)

#passed
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a>35 or b>35)

#10 to 50
a=int(input("enter a:"))
b=int(input("enter b:"))
print(a>=10 and b<=50)

#not equal to zero
a=int(input("enter a:"))
print(a!=0)

#membership operators
#in
y="name"
print('a' in y)

#python
list=["java","c++","python"]
print("python" in list)

#number
list=["1","2","3","4","5"]
print("1" in list)

#not pressent
string=["a","b","C"]
print("d" not in string)


#identity operators
#is , is  not
a=10
b=10
print(a is b)

#identity
a=['1','2','3','4','5']
b=a
print(a is b)

#check
x=['1','2','3','4','5']
y=x
print(x is y)

#is not
a=['1','2','3','4','5']
b=a
print(a is not b)

#Bitwise operator
a=10
b=5
print("AND:",a&b)
print("OR:",a|b)
print("XOR:",a^b)
print("~a:",~a)

#Real time mini task
name=str(input("enter a name:"))
s1=float(input("enter s1  mark:"))
s2=float(input("enter s2  mark:"))
s3=float(input("enter s3  mark:"))
s4=float(input("enter s4  mark:"))    
s5=float(input("enter s5  mark:"))
total=s1+s2+s3+s4+s5
average=total/5
print(total)
print(average)
p=35
if s1>35 and s2>35 and s3>35 and s4>35 and s5>35:
    print("Pass")
else:
    print("fail")

#eletricity bill
units=int(input("enter a units:"))
rate=5
bill=units*rate
print("electricity bill",bill)

#shopping
price=int(input("Enter product price:"))
quantity=int(input("Enter quantity:"))
total=price*quantity
if total>=1000:
    discount=total*10/100
else:
    discount=0
final=total-discount
print("Total Amount:",total)
print("Discount:",discount)
print("Final Amount:",final)

#voting eligibility
age=int(input("Enter your age:"))
if age>= 8:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


#login validation
username=input("Enter username:")
password=input("Enter password:")
if username=="admin" and password=="1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#even or odd
num=int(input("Enter a number:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")
'''
#number comparision
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
    print("Largest:",a)
elif b>=a and b>=c:
    print("Largest:",b)
else:
    print("Largest:",c)


