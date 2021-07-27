#EXERCISE 2 - Summing numbers

def mysum(num):
    t = 0
    for num in num:
        t += num
    return t
    

n = int(input('how many number you want to add'))
list1 = []
for i in range(0,n):
    a = int(input())
    list1.insert(i,a)

print(mysum(list1))
