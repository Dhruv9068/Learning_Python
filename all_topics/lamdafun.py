# python support a function name lamda function can make the code more shorter


print("code with normal function  of factorial")


import math

def fact(n):
    if n==1:
        return 1
    else:
        return (n * fact(n-1))

n=int(input('enter number for factorial\t'))
res=fact(n)
print(res)



print('same with lamda function')

""" syntax 
lambda argument:iteration"""


res1=(lambda n: 1 if n==1  else n* fact(n-1))

n=int(input('enter num for factorial with lamda fun\t'))
print(res1(n))



# another

# normal functiom


print("increment using normal function")
def add (a):
    return a+1
res= add(5)
print(res)


print("increment same input using lambda")

lm=lambda a: a+1
print(lm(5))


print("two arguments")
lm=lambda a,b: a+b
print(lm(5,6))
