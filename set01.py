eg1={10,20,30}
print(eg1)
eg2={10,20,30,20,30,10,30,30,20}
print(eg2)
eg3={"likhith",143,"some_xyz",True}
print(eg3)
eg4={}
print(eg4)
print(type(eg4))
print(type(eg3))
print(type(eg2))
print(type(eg1))
# print(eg1[5])        #?slicing and indexing is not available in set datatype in python 
# print(eg1[1:2])      as it won't store in insertion order !  
print("-----01-----")
s1={"d","e","e","p","a","k"}
for i in s1:
    print(i)
print("-----02-----")
for i ,j in enumerate(s1):
    print(i,j)

print("-----03-----")
for i ,j in enumerate(s1):
    print(i,j,hash(j))

print("-----04-----")
for i ,j in enumerate(eg1):
    print(i,j,hash(j))


print("-----05-----")
s2={0.1,0.2,0.3,0.5555555}
for i ,j in enumerate(s2):
    print(i,j,hash(j))

print("-----06-----")
s3={True,False,None,1,2,0}
for j in s3:
    print(j,hash(j))

