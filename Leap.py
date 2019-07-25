n=int(input())
if((n%400==0) or ((n%4==0) and (n%100 !=0))):
    print("Leap")
elif((n%400!=0) or ((n%4!=0) and (n%100 ==0))):
    print("Not Leap")
else:
    print("Invalid Input")
