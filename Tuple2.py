t=(10,20,30,40,50)
                      
t1=t[:2]+(25,)+ t[2:]   # Insertion in tuple using an 3rd variable
print(t1)

t2=t[:2]+ t[3:]          # Deletion in tulpe by using 3rd variable
print(t2)

t3=((1.1,1.2,1.3,1.4,1.5),(2.1,2.2,2.3,2.4),(3.1,3.2,3.3))
print(len(t3))
print(len(t3[0]))
print(len(t3[1]))
print(len(t3[2]))
print(t3[0][3])