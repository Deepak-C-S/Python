def prime(num):
    count=0
    i=1
    if num==1:
        return f"{num} -> not a prime number"
    while i<=num:
        if num%i==0:
            count+=1
        i+=1
        if count>2:
            return f"{num} -> it is not a prime number"
    if count==2:
        return f"{num} -> it is prime number"
n=int(input("enter the number to check the prime number"))
print(prime(n))