n,m=list(map(str,input().split()))
s=1
if(n.isdigit() and m.isdigit()):
    n=int(n)
    m=int(m)
    for i in range(0,m):
        s=s*n
    print(s)
else:
    print("Invalid Input")
