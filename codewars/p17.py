def gcd_(n,m):
    lower=n
    gcd=1
    loopc=0
    if m<n:
        lower=m
    for i in range(2,lower+1):
        loopc+=1
        if n%i==0 and m%i==0:
            gcd=i
    return f"the gcd of {n} and {m} is {gcd} \n with loop count {loopc}"
n=int(input("enter the number 1 to check the hcf: "))
m=int(input("enter the number 2 to check the hcf: "))
print(gcd_(n,m))
