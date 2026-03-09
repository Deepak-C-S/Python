def rec_asn(n,power,temp,asn=0):
    if n<=0:
        return asn==temp
    base=n%10
    asn+=base**power
    n//=10
    return rec_asn(n,power,temp,asn)
    
data=int(input("enter"))
power=reccountnum(data)
flag=rec_asn(data,power,data)
if flag:
    print(f"the {data} is asn number")
else:
    print(f"{data} is not a asn")