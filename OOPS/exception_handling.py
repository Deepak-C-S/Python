try:
    n=int(input("num 1: "))
    m=int(input("num 2: "))
    print(f"{n} by {m} is {n/m}")

except Exception as error:
    print("error is ",error)
