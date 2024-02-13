''' types of runtime errors

ZeroDivisionError -  raised when you try to divide a number by zero.
TypeError -  raised when you try to perform an operation or function on an object of incorrect type.
IndexError -  raised when you try to access an index that is out of range of a list or other sequence.
KeyError -  raised when you try to access a key that does not exist in a dictionary.
ValueError -  raised when a function or operation receives an argument of the correct type but an inappropriate value.
NameError -  raised when a variable or function name is not defined in the current scope.
AttributeError -  raised when you try to access an attribute of an object that does not exist.
FileNotFound -  raised when a file or directory cannot be found.
KeyboardInterrupt -  raised when the user interrupts the program execution, usually by pressing Ctrl+C.
MemoryError -  raised when a program runs out of memory.

'''

''' syntax of error handling
try:
try the codde you have error expected must be run time error

except
which error it you expect  must be run time error

finally:

 after knowing you have error or not'''




# for example to check code have zero division error or not

try:
    a=2
    b=0
    c=a/b

except ZeroDivisionError:
    print('yes you have error')

finally:
    print('you find it')



# this below code is not handle the syntax error becouse it is not a runtime error
'''try:
    a=2
    b=3
    c=a/b

except SyntaxError:
    print('yes you have error')

finally:
    print('you find it')'''



