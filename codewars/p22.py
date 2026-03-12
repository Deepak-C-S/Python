def is_isogram(string):
    s=string.lower()
    check=[]
    for i in s:
        if i in check:
            return False
        else:
            check.append(i)
    
print(is_isogram("adsa"))