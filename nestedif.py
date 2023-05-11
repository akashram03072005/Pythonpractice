#1.leap year:

year=int(input("enter the year"))
if (year%400==0)and(year%100==0) :
    print("0 is leap year",year)
elif(year%4==0)and(year%10!=0) :
    print("0 is leap year",year)
else:
    print("0 ios not a leap year",year)
    
