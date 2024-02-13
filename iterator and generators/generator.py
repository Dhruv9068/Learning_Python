def fun ():
    yield 1
    yield 2
    yield 3

value=fun()
print(next(value))
print(next(value))
print(next(value))


#or use

for i in value:
    print(i)


print('now print squares using generator')
def square():
    n=1
    while n<=5:
        square=n**2
        yield square
        n+=1
val=square()

for i in val:
    print(i)
