import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)    
print(type(phonebook))

phone = phonebook['Chris']

print(phone)

print(len(phonebook))

mydictionary = dict(m=8, n=9)

print(mydictionary)

mydict = {}

print(mydict)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(phonebook[name])
else: 
    print(name, 'not found')





print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123' #just an update
phonebook['Joe'] = '555-4444' #an append
print(phonebook)

#cannot update the key 




print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris']
#print(phonebook) 
#if does not exist you will get an error 

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


#default is to iterate just through keys 
for key in phonebook:
    print(key)
    print(phonebook[key])

for value in phonebook.values():
    print(value)

for k,v in phonebook.items(): 
    print('Key:', k, '   Value: ', v)

for tuple in phonebook.items():
    print(tuple)

#tuple is () and list is [] dictionairies are immmutable 

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("chris","key not found") #is case sensitive 
print(phone)

#phonebook.clear()
#print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#remove = phonebook.pop('Chris','key not found') #if not there you get key not found msg 

#print(remove)
#print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#a = phonebook.popitem()

#print(a)
#print(phonebook)

#just picks the last value of the dictionary 


print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])


print()
print('*****  end section 9 ********')
print()








