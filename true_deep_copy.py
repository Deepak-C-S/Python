dictt={
    "name":"Deepak",
    "age":22,
    "address":{"pres":"Laggere","prem":"Kadur"},
    "marks":{"701":100,"702":95,"714":89}
}
print(dictt)
print(dictt["name"])
d1=dictt.copy()  #! deep copy
print("d1",d1)
dictt["address"]["pres"]="Bengaluru"
print(dictt)
print(d1)