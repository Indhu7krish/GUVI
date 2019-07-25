m,n=list(map(str,input().split()))
l=[]
if(n.isdigit() and m.isdigit()):
    n=int(n)
    m=int(m)
    for j in range(m+1,n):
        s=0
        k=j
        while(j>0):
            r=j%10
            s=s+(r*r*r)
            j=j//10
        if(s==k):
            l.append(k)
    print(*l)
else:
    print("Invalid Input")
