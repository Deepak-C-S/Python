data=set()
n=int(input("enter how many value u need to insert :"))
for i in range(n):
    a=int(input("enter element to insert :"))
    data.add(a)                                                             #? .add( )   to add one element
print(data)

print("enter ")
a1=list()
n1=int(input("enter how many value u need to insert :"))
for i in range(n1):
    a=int(input("enter element to insert :"))
    a1.append(a)
data.update(a1)                                                             #? .update( ) to add multiple element .update([1,2,3])
print(data)

dele=int(input("enter hval to delete:"))
data.discard(dele)                                                          #? .discard( ) to delete element
print(data)