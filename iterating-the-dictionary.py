student={
    "Name":"Deepak",
    "USN":"1CE22AI012",
    "Dept":"AIML",
    "Age":22
}
print(student)
print("the lenght of student dictionary is :",len(student))
print(student["Age"])

for i in student:
    print(i)

for i in student.keys():
    print(i)

for i in student:
    print(student[i])

for i in student.values():
    print(i)

for i in student:
    print(i, student[i])

for i in student.items():
    print(i)
