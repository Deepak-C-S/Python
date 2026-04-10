 #TODO                             INBUILD FUNCTION

s1={1,2,3,4}
s2={3,4,5,6}  
print(s1)
print(s2)
s3=s1.union(s2)                      #? union : to combine two sets and remove duplicates .union(s2) or s1|s2
print(s1|s2)                                              
print(s3)                                               
s4=s1.intersection(s2)              #? intersection : to get common element from two sets .intersection(s2) or s1&s2
print(s4)
s5=s1.difference(s2)                #? difference : to get elements from s1 that are not in s2 .difference(s2) or s1-s2
print(s5)
s6=s2.difference(s1)                #? difference : to get elements from s2 that are not in s1 .difference(s1) or s2-s1
print(s6)
s7=s1.symmetric_difference(s2)      #? symmetric_difference : to get elements that are in either s1 or s2 but not in both .symmetric_difference(s2) or s1^s2
print(s7)    #?D
 # -------------------------------------------------------------------

t1={1,2,3,4}
t2={3,4,5,6}
t3={5,6,7,8}

print(t1.isdisjoint(t2))            #? isdisjoint : to check if two sets have no common elements  t1.isdisjoint(t2)
print(t2.isdisjoint(t3))
print(t3.isdisjoint(t1))

t4={1,2,3,4}
t5={1,2}
print(t4.issuperset(t5))            #? issuperset :
print(t5.issuperset(t4))
print(t4.issubset(t5))
print(t5.issubset(t4))

    #? keyword for forzenset
    #? forzenset
t6=frozenset([10,20,30,40])
print(t6)
#t6.add(60)       #! error 
#t6.discard(10)   #! error

#t7={10,20,[30,40],50}     #! error
#t8={10,20,{30,40},50}     #! error
t9={10,20,30,(40,50),60}
print(t9)
