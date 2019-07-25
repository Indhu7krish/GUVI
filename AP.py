n,a,d=list(map(str,input().split()))
if(n.isdigit() and a.isdigit() and d.isdigit()):
    n=int(n)
    a=int(a)
    d=int(d)
    s=(n*((2*a)+((n-1)*d)))//2
    print(s)
else:
    print("Invalid Input")
