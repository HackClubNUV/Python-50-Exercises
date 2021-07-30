#Exercise 9 - First-last - (Print first and last elements of inputs like strings,tuples,lists)

def fl(seq):
    return seq[:1] + seq[-1:]

#For string
print (fl(input("Enter a string :")))

#For tuple and list
print(fl(eval(input("Enter a tuple or list :"))))
