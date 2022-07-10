#leap year
year=int(input("enter a year"))
if (year%4==0) and (year%100!=0) :
    print("its leap year")
elif (year%400==0 and year%100==0): 
        print("it is century leap year")
else:
    print("not leap year")
    
