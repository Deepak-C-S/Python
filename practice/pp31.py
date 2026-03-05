def c(n):
    temp=n
    c=0
    neg=0
    if n<0:
        n*=-1
        neg+=1
    while n>0:
        n//=10
        c+=1
    return c,neg
i=int(input())
c,n=c(i)
if n==0:
    print(f"{i} is positive and it contain {c}")
else:
    print(f"{i} is negative and it contain {c}")