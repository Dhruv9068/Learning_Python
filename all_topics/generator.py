def fun ():
    yield 1
    yield 2
    yield 3

value=fun()
print(next(value))
print(next(value))
print(next(value))

a = int(input())
b = int(input())

add=a+b
sub=a-b
mul=a*b
print(add +'\nsub')
print(sub +'\nmul')
print(mul)