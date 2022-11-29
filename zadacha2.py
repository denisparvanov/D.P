a=int(input("Vavedi chislo"))
s=0
for g in range(1,a+1):
    n=0
    for l in range(0,g):
        n=n*10+a
        print(a,end="")
    print("+",end="")
    s+=n
print("="+str(s))

