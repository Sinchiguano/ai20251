

# pairs key and the other value

myDictionary={'cat':'cute','dog':'friend','donkey':'hard-working'}

print(myDictionary['donkey'])


print('cat' in myDictionary)

myDictionary['fish']='wet'

for key in myDictionary:
    value=myDictionary[key]
    print('The %s is %s'%(key,value))

print("ANOTHER WAY TO PRINT DICTIONARIES")

for key, value in myDictionary.items():
    print('the %s is %s '%(key, value))


# dictionary={'1':1, '2':4.........}

myDictionary1={i:i**2 for i in range(20)}
print(myDictionary1)



print('set container')
animals={'cat','dog','chicken','hen','monkey'}
print('fish' in animals)
animals.add('fish')
print(animals)
animals.add('mouse')
print(animals)

numberOfElements=len(animals)
print(numberOfElements)

animals.remove('cat')
print(animals)
print(type(animals))
print(len(animals))

print('TUPLES')
tupleData=(5,15,5)
print(type(tupleData))

aux=list(tupleData)
aux.remove(15)
tupleData=tuple(aux)
print(tupleData)