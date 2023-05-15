

# functional programming
''' python is a language support functional programming


means

1) a function can be assign to a variable and pass value to varibale in python
2)a function can be pass as a argument to another function in python
3)a function can return another function in python'''



#1  normal function

def add (i,j):
    return i+j
res=add(1,2)
print(res)



#2) assign function to varibale and pass values to it
print("output is still same")
a=add
res=a(1,2)
print(res)


#3) return function to another function

print("now passing function in return")
def call (i,j):
    return add(i,j)

res=call(1,2)
print(res)


#4) passing function to function


print("pass func to func-square the add function result")
def fun (i,j,fn):
    return call(i,j)**2

res=fun(1,2,call)
print(res)
