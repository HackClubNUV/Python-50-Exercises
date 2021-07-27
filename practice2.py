def mysum(*num):
    t = 0
    for num in num:
        t += num
    return t
    
print(mysum(1,2,3))
print(mysum(10,20,30,40))

