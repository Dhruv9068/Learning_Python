
#tuples are semilar to list but elements in tuple defined in () and tuple is immutable in nature


#example 1

num=(1,2,3,4,5)
print(num)

#o/p = (1,2,3,4,5)

#example 2
num=(1,2,3,4)
print(num[1])

#o/p= 2


#example 3 contetinate two tuples

tup1=(1,2,3)
tup2=("mike",1,2,'3')

print(tup2+tup1)

#o/p=('mike', 1, 2, '3', 1, 2, 3)




'''tuple are immutable that is you cannot change element of tuples ones defined
like
t=(!,2,3)
t[1]=0

o/p=error'''

#sorting in tuple

tup=(1,4,3,5,6,2,9,8)

print(sorted(tup))

#o/p = [1, 2, 3, 4, 5, 6, 8, 9]


#to get index of element

print(tup.index(9))
#o/p=6

\


