n=input()
n=n.lower()
c=0
if(n.isdigit()):
    n=int(n)
    while(n>0):
        n=n//10
        c=c+1
    print(c)
else:
    print("Invalid Input")
