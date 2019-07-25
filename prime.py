n=input()
s=0
if(n.isdigit()):
    n=int(n)
    for i in range(1,n+1):
        if(n%i==0):
            s=s+1
    if(s<=2):
        print("yes")
    else:
        print("no")
else:
    print("Invalid Input")
