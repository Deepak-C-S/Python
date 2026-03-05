def eo(n):
    return n%2==0
n=int(input("enter the number : "))

# while num>0:
#     flag=eo(num)
#     if flag:
#         print(num,end=" ")
#     num-=1

# print("even")
# for i in range(1,num+1):
#     flag=eo(i)
#     if flag:
#         print(i,end=" ")
# print("\nodd")
# for i in range(1,num+1):
#     flag=eo(i)
#     if not flag:
#         print(i,end=" ")
count=n
num=1
while count>0:
    flag=eo(num)
    if flag:
        print(num,end=" ")
        count-=1
    num+=1