


''' why list is needed

list is needed to reduce the use of more number of variables
list is specified by its element index value
'''

# now taking different types of list
#list of numbers 1 < 5

list1=[1,2,3,4]
#index 0 1 2 3

print(list1[1])


print(list1[3])


# list of strings

list2=['red','helo','hi','bye']


for x in list2:
    print(x)


# list of mixture

list3=['no',3,(5,4),'dhruv']
print(list3)
print(list3[2])

# taking list as a element of another list
list4=['yes',3,list1]
print(list4)




# list functions


l=['mike',10.5,9]

#function1
l.append(10)
print('after append 10 list is\n', l)

#function2
l.extend([8,20])
print('after extend 8 and 20 in list becomes\n', l)
# function 3

l.remove(10)
print('after removing 10\n',l)

#function 4

del l[0:2]

print('after deleting 0 and 2 nd index of list\n',l)

# function 5
'''l.clear()
print('after clear the list\n',l)'''

# function 6

l.pop(2)

print('after deleting the index 2 value \n', l)

# function 7

l.insert(1,'dhruv')
print('after inserting dhruv at index 1\n',l)


l.remove('dhruv')
l.append(5)


#function 8

l.sort()
print('list become sorted\n',l)

#function 9

l.reverse()
print("list is reversed\n",l)

#function 10

print('\nindex value of 5 is ',l.index(5))

#function 11

print('\nlenegth of list is', len(l))
