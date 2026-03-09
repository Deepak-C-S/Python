def rec_rev(n,m=0):
    if n<=0:
        return m
    m=(m*10)+n%10
    n//=10
    return rec_rev(n,m)
data=int(input("enter"))
k=rec_rev(data)
print(f"the reverse of {data} is {k}")