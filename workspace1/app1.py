
# def prediction(age):
#     age=age+10
#     return age

# def niceMesage(agePredicted,name):
#     print(f'You name is {name} and your age after 10 years is {agePredicted}')
    

# while True:
#     name=input("Enter your name please!")
#     age=int(input("Enter your age!!!"))

#     agePredicted=prediction(age)
#     niceMesage(agePredicted, name)


print('CONTAINERS LIST')


listNumbers=list()
listNumbers.append(3)
listNumbers.append(1)
listNumbers.append(2)

for item in listNumbers:
    print(item)

print(listNumbers[-1])



listNumbers[-2]='Cesar'
for item in listNumbers:
    print(item)
print('***************************')
print('before pop')
listNumbers.append('bar')
for item in listNumbers:
    print(item)

print('after pop')


lastItem=listNumbers.pop()
print("list: ",listNumbers)
print('lastItem')


print('*************')
listNumbers1=list(range(30))
print(listNumbers1)


itemsSeleted=listNumbers1[10:21]
print('-------------')
print(itemsSeleted)
# itemsSeletedChanged=list()
# for i in itemsSeleted:
#     itemsSeletedChanged.append(i+10)
# print (itemsSeletedChanged)

listNumbers1[10:21]=itemsSeleted
print('new list')
print(listNumbers1)




evenList=[i for i in range(10) if i%2==0]
print(evenList)


firstList=list(range(20))
secondList=[i**2 for i in firstList ]
print('firstList')
print(firstList)
print('secondList')
print(secondList)