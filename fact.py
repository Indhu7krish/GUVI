n=input()
s=1
if(n.isdigit()):
    n=int(n)
    for i in range(n,1,-1):
        s=s*i
    print(s)
else:
    print("Invalid Input")
