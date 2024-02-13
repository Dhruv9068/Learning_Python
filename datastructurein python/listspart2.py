

# list slicing



list1=[1, 'mike',1980,50,60,70,80]
l=[10,20,30,40,50,60,70,80]

print(list1[0:5])
print(list1[2:7])
print(l[0:6:2])



#list comprehension

'''l=[10,20,30,40,50]
for i in range(1,11):
    print(l[i-1])'''

x=[]

for i in range(11):
    z=i**2
    x.append(z)
print(x)


# list comprehension

x=[i**2 for i in range(11)]
print(x)


x=[]
for i in range(11):
    if i%2==0:
        z=i**2
        x.append(z)
print(x)

#list comprehension


x=[i**2 for i in range(11) if i**2%2==0]
print(x)


