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
    b=len(a)
    c=(b//2)+1
    print(c)
else:
    print("Invalid Input")
