# shallow copy
a=["d","e","e","p","k"]
print("before")
print(a)
d=a
d.append("c")
d.append("s")
print("after")
print(d)
print(a)


#deep copy
A=["D","E","E","P","A","K"]
print("before")
print(A)
D=A.copy()
D.append("C")
D.append("S")
print("after")
print(D)
print(A)