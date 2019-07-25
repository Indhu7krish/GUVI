n=input()
if(n.isdigit()):
    n=int(n)
    a=list(map(int,input().split()))
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if(i!=j):
                if(a[j]>a[i]):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
    print(*a)
else:
    print("Invalid Input")
