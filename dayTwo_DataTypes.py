#This is the dnamey two of lenamerning python namend in this progrnamem we're going to lenamern namebout the dnametname types 
# Text Type String
name= "Jhon" #in py we dont need to specify the datatype as it will automatically detect the datatype of a declared vairable
print("The name of name person is:" + name)
print(type(name))

#2
#Numeric Data Types of Python
# there are 3 numeric data types in python that are int, float and complex

#Program for int
num_one= 5
num_two=10
print("The data type of above declared vairables is:",type(num_one),type(num_two))
#py cannot directly concate a number to string directly,so
print("The sum of " + str(num_one) + " and " + str(num_two) + " is: " + str(num_one+num_two))
print("The sum of two numbers is: " , num_one+num_two)
print(num_one+num_two)
print(num_one,num_two)

# program for float
# float means the values that are on points , for eg: 3.1415, 7.99 ,etc
num1=5.5
num2=3.7
num3=num1+num2
print(type(num2))
print(num3)

# program for complex(list, tuple, set,dict,)
# complex datatypes are those which holdes multiple values in it. Major types are list, tuple, set,dict
# List=Collection of multiple data
# tuple=immutable data which cannnot be unchanged or unmuted
# set=mutable data which can be unchanged
# dict= Similar to mapping function which stores data in key value pair
# {} is used for dictionary and sets 
# [] is used for list and indexes


list_fruits=['apple','banana','mango']
list_fruits[1]="kiwi"
print(list_fruits)
 #prints the value of index 1 at list of fruits i.e banana

# tuple is unchangable after declaration
numbers=('one','two', 'three','four')
print(numbers)
# numbers[1]='yellow' this is wrong approach

# set is collection of unique items in an specific order which doesnt allows duplicate data and supports the data in any order
setNumbers={1,2,3,4,4} #Output is {1,2,3,4} as the duplicated data are removed
setNumbers.add(7)
print(setNumbers)
print(type(setNumbers))

# dict is a datatype that stores the data in an key value pair i.e keys are unique for all the values
students={
    'name':'max',
    'age':'19',
    'address':'lalitpur'
          }
print(students)
print(type(students))

#range is another datatype that represents the squence of the numbers
numRange=range(10)
print(type(numRange))
print(numRange)

# another one is we have set types which is 
# 1. set -> It is mutable or changeable similar to example of above set
# 2. frozenset -> It is immutable which is not changeable once declared

fs=frozenset({1,2,3,4,5})
print(type(fs))
# fs.add(6) This will throw and error as its not mutable

# bool returns the boolaean value i.e True or False
x=10
y=20
print(x>y) #Output: False

# Binary Types
# 1. bytes -> Immutable Values   "b" keyword is used here

bytesExample=b"hello"
print(bytesExample)
print(bytesExample[1])

# 2. bytearray -> Collection of multiple bytes here
bytearrayExample= bytearray(b"Max")
print(bytearrayExample)
# print(bytearrayExample[2])

bytearrayExample[2]=105 
print(bytearrayExample)

# memoryview let's us change the value of an bytearray without making the copy of the data

data=bytearray(b'namaste')
mvExample= memoryview(data)
print(mvExample)

# None keyword is used when there are no any values known to us
noneData=None
data=45
print(data)