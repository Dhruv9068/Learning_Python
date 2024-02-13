

# code resuebility

def function():
    print("hello")
    print('pythom')
function()


str1='hello'
str2='world'
def add_strings ( ):
    print(str1 +" "+ str2)
add_strings()




# return statement use

def add(a,b):
    c=a+b
    return c
value=add(10,20)
print("the sum is ",value)

def mulf(a,b):
    c=a*b
    return c
value=mulf('dhruv\t',3)
print('lets print string 3 times',value)


# passing values/parameters to function

def func1(a):
    a+=1
    print(a)
func1(5)


#passing two parameters

def add(a,b):
    print(a+b)
add(5,10)

# passing function as argument
# question : sqaure a number of sum of given input
def add(a,b):
    return a+b
def sqr(z):
    return z*z

result=sqr(add(5,10))
print(result)