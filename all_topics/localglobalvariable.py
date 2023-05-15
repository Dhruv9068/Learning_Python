


#Local variable - is variable defined local to the block

n=2

def func():
    n=6    # here this n is local to the function func
    print(n)


func()
print(n)


n=2

def func():
    global n    # here this n is local to the function func
    print(n)


func()
