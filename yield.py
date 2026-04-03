# def fn():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# s=fn()
# # print(s.__next__()) # next one methgod 

# # print(next(s))    # next another methgod 
# # print(next(s))
# # print(next(s))
# # # print(next(s))
# for i in s:
#     print(i)
def fn2():
    n=1
    while(n<=10):
        sqr=n*n
        yield sqr
        n+=1
res=fn2()
print(next(res))
print(next(res))
print(next(res))
print(next(res));print(next(res))