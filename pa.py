n=input()
s=0
if(n.isdigit()):
    n=int(n)
    m=n
    while(n>0):
        r=n%10
        s=(s*10)+r
        n=n//10
    if(m==s):
        print("Yes")
    else:
        print("No")
else:
    print("Invalid Input")
