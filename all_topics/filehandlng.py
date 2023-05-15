

#opening and perform reading on file
'''
file1=open('file.txt','r')

reading=file1.read(5)
print(reading)
file1.close()


#type2 read lines
file1=open('file.txt','r')

reading=file1.readlines()
print(reading)
file1.close()

#type 3 read a line
file1=open('file.txt','r')

reading=file1.readline()
print(reading)
file1.close()
'''

print('\n\n#now its write operation:-')
''' write mode 
        whenever we use write mode it erase the existing data and store a new data you have engtered to write'''

'''
file2=open('file.txt','w')

writing = file2.write('mera nam dhruv hai \n'+ "mai btech krraha hu 2nd year\n"+ 'aapka nam kya hai')

file2.close()


file2=open('file.txt','r')
reading=file2.read()
print(reading) 
file2.close()
'''






print('\n\n#now its Append operation:-')
''' Append mode 
        whenever we use append mode file data remain same & it add a new data you have entered to write'''


'''file2=open('file.txt','a')

writing = file2.write('\nhello')

file2.close()


file2=open('file.txt','r')
reading=file2.read()
print(reading)'''


print('\n\n#now its r+ operation:-')
''' r+ mode 
        this mode allows us to use both functions read and write instead of using r and w we can use r+'''


file2=open('file.txt','r+')

writing = file2.write('\nhello my name is dhruv')
file2.close()
file2=open('file.txt','r+')
reading=file2.read()
print(reading)
file2.close()