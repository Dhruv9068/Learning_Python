

dict={'key1':2,'key2':'magic','key3': (3,4),'key5': [5,4]}
print(dict)

print(dict['key3'])



# disctionary funtions


dict['key6']='hello'
print(dict)
del dict['key2']
print(dict)


print(dict.get('key4'))
print(dict.get('key8'))



print(dict.keys())

print(dict.values())

print('key2' in dict)
print('key5' in dict)