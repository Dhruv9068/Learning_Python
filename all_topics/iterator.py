# iterator is used to print iteration


list=[1,2,3,4,5,6]

iterations=iter(list)

print(iterations.__next__())
print(iterations.__next__())
print(iterations.__next__())
print(iterations.__next__())
print(iterations.__next__())
#another way
print(next(iterations))
