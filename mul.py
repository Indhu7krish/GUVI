n=input()
l=[]
if(n.isdigit()):
    n=int(n)
    for i in range(1,6):
        l.append(n*i)
    print(*l)
else:
    print("Invalid Input")
