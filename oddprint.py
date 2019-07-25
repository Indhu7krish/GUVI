m,n=list(map(str,input().split()))
s=0
l=[]
if(n.isdigit() and m.isdigit()):
    n=int(n)
    m=int(m)
    for i in range(m+1,n):
        if(i%2!=0):
            l.append(i)
    print(*l)
else:
    print("Invalid Input")
