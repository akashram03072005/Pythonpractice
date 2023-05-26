size=int(input("enter the value :"))
for i in range(1, size+1):
    for j in range (size-i):
        print(" ", end=" ")
    for k in range(2* i -1):
        print("*", end=" ")
    print()

size = int(input("enter the value:"))
for i in range(size,0,-1):
    for j in range(0,size-i):
        print(end=" ")
    for k in range(0,i):
        print("* ", end=" ")
    print()

size=int(input("enter the size:"))
for i in range(0, size):
    for j in range(1, i + 1):
        print("* ", end="")
    print("\r")
for i in range(size, 0 , -1):
    for j in range(2, i + 2):
        print("* ", end="")
    print("\r")

number =int(input("enter the value"))
sum=0
sqr=number*number
print("square of the given number:",sqr)
while(sqr>0):
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
print("sum of the given number:",sum)
if(sum==number):
        print("number is neon")
else:
   print("number is not nenon")
number=int(input("enter the number"))
n=number
sum=0
rem=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of the given number",sum)
if (number%sum==0):
    print(number,"it is a niven number")
else:
    print(number,"it is not a niven number"

print("Enter the Number: ")
num = input()
num = int(num)
print("Factors of", num)
i = 1
while i<=num:
    if num%i==0:
        print(i)
    i = i+1

