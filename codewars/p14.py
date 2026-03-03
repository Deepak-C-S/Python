def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return f"{num} is a prime number"
    else:
        return f"{num} is not a prime numbers"
n=int(input("enter the number to check the prime number"))
print(prime(n) )