#note filter are not effective for normal function it only give disrable output of conditional
# for normal we use map but that are not effective for conditional


# syntax
# output type map(fun, range/sequnce)



res=set(map(lambda a:a**2,range(5)))
print(res)


print('sum two ranges of 0 to 4')
res=set(map(lambda a,b:a+b ,range(5),range(5)))
print(res)

print('random set')
num={3,4,5,6}
res=set(map(lambda a:a*3 ,num))
print(sorted(res))


