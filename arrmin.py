n=input()
if(n.isdigit()):
    n=int(n)
    a=list(map(int,input().split()))
    for i in range(0,len(a)):
        m=a[i]
        for j in range(0,len(a)):
            if(i!=j):
                if(a[j]<m):
                    m=a[j]
    print(m)
else:
    print("Invalid Input")
