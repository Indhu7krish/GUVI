m,n=list(map(str,input().split()))
l=[]
if(n.isdigit() and m.isdigit()):
    n=int(n)
    m=int(m)
    for j in range(m+1,n):
        s=0
        for i in range(1,j+1):
            if(j%i==0):
                s=s+1
        if(s<=2):
            l.append(j)
    print(*l)
else:
    print("Invalid Input")
