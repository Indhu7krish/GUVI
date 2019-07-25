n=input()
s=0
if(n.isdigit()):
    n=int(n)
    m=n
    while(n>0):
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if(s==m):
        print("yes")
    else:
        print("no")
else:
    print("Invalid Input")
