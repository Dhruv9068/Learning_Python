


# when a function calling itself is callled recursion


# Code 1:-
'''import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(50)     # use to limit the recursion infinite call default it is 1000
print(sys.getrecursionlimit())
def unstopcall():
    print('Dhruv')
    unstopcall()

unstopcall() '''


#Code 2:-


'''import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(50)     # use to limit the recursion infinite call default it is 1000
print(sys.getrecursionlimit())
n=0
def unstopcall():
    global n
    n=n+1
    print('Dhruv',n)
    unstopcall()

unstopcall()'''



#Code 3    Factorial program

def fact(n):
    if n<2:
        return 1
    else:
        return n * (fact(n-1))

n=int(input("enter n\n"))
result=fact(n)
print('the factorial of %d is %d '%(n,result))

'''or     
print('the factorial is ', fact(n))'''



#program for fibbonacci

