#!/usr/bin/env python3
# HELLO WORLD 
# THIS IS THE WAY TO CREATE COMMENTS

# ctrl + k + c to comment severals lines

# ctrl + k + u to uncomment several lines
print('THIS IS MY FIRST MESSAGE....')


variable1=12
variable2=12.0
variable3=True
variable4='CESAR SINCHIGUANO'


print(variable1)
print(variable2)
print(variable3)
print(variable4)


# LIST
print('# LIST')
list1=[1,3,4,5,6,7,'CESAR',True]
print(list1[5])
print(list1[6])

# DICTIONARY
print('# DICTIONARY')
dict1={'student1':'cesar sinchiguano','student2':'wilmer fueres'}
print(dict1['student2'])


stringVariable='3'
print(type(stringVariable))
numericalVariable=int(stringVariable)
print(type(numericalVariable))

print('----------------------------')
print("control flow")


age=30
message1='you are young'
message2='you are old'

if age>=25:
    print(message2)
else:
    print(message1)
    





if age>30:
    print(message2)
elif age<30:
    print(message1)
elif age==30:
    print('you have the right age, congratulations')


print('*****************')    

for i in list1:
    print('Elements inside the list',i)

print('how to iterate in dictionary')
for key in dict1:
    print(dict1[key])


print('FUNCTIONS')
print('----------------')

def message():
    print('hello from the function message')


message()
for i in range(10):
    message()


# name=input('Enter your name:')    
# age=int(input('Enter your age:'))


# def message1(age, name):
#     print("You are young!!!")
#     print(f'Your name is {name} and your age is {age}')

# def message2(age,name):
#     print('You are old!!!')
#     print(f'Your name is {name} and your age is {age}')

# def message3(age,name):
#     print('You are in the right age!!!')
#     print(f'Your name is {name} and your age is {age}')

# if age<30:
#     message1(age,name)
# elif age>50:
#     message2(age, name)
# else:
#     message3(age,name)

# def message1(age, name):
#     print("You are young!!!")
#     print(f'Your name is {name} and your age is {age}')

# def message2(age, name):
#     print('You are old!!!')
#     print(f'Your name is {name} and your age is {age}')

# def message3(age, name):
#     print('You are in the right age!!!')
#     print(f'Your name is {name} and your age is {age}')

# while True:
#     name = input('Enter your name: ')    
#     age = int(input('Enter your age: '))

#     if age < 30:
#         message1(age, name)
#     elif age > 50:
#         message2(age, name)
#     else:
#         message3(age, name)


list1=[1,2,3,4,5]
listsquared=[]


for item in list1:
    listsquared.append(item**2)

for item in listsquared:
    print(item)


import math
listsquarenumbers=[]

for item in list1:
    listsquarenumbers.append(math.sqrt(item))

print('SQUARE ROOT FROM MY LIST')
for i in listsquarenumbers:
    print (i)
    