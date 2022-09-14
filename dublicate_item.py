lst = [1,1,20,35,46,7,35,1,5,89,43,5,43]

for item in lst:
    for i in range(lst.count(item)-1):
        lst.remove(item)
lst.sort()
print(lst)