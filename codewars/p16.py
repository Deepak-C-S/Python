def prime(n):
    i=1
    count=0
    cc=0
    while(i*i<=n):
        cc+=1
        if n%i==0:
            #print(i,end=" ")
            count+=1
            if i!=n//i:
               # print(n//i,end=" ")
                count+=1
        i+=1
        if count==2:
            return "prime"
        else:
            return "not a prime"
n=int(input("enter"))
print(prime(n))