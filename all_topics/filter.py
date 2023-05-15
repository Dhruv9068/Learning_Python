# filter contain two arguments

# filter are used get conditional function output in desirable format - list, tuple, set etc

# syntax  filter(function,sequence/range)

def even(a):
    return a%2==0

num={1,2,3,4,5,6}


res=set(filter(even,num))

print(res)


print('filter with lamda ')

res=set(filter(lambda a:a%2==0 ,num))
print(res)


print("provinding range now")

res=set(filter(lambda a:a%2==0 ,range(0,21)))
print(res)


#note filter are not effective for normal function it only give disrable output of conditional for normal we use map but that are not effective for conditional
