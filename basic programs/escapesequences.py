


#raw string r use to ignore escape sequences
print("hello \"world\" i am here")

print(r" hello \"world\" i am here")

print("hello \t world")
print("hello \fWorld")


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 


print("blackslash print \\")


