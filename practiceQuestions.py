# #  Practice question 1
# Program to input 2 numbers and print their sum
numOne= int(input("Enter Number One: "))
numTwo= int (input("Enter Number Two: "))
sum=numOne+numTwo
# print("The sum of num1 and num2 is: " , sum)
print(f"The sum of {numOne} and {numTwo} is: {sum}")
print("--------------------Break-----------------------")


#Practice Question 2
#Program to input side of a square and print its area
side=int(input("Enter the value of a side: "))
print(f"The area of a square whose side is {side} is {side*side}")
print("-------------------Break------------------------")

#Practice Question 3
#Program to input 2 floating point numbers and print their average
fnumOne=float(input("Enter any float number one: "))
fnumTwo=float(input("Enter any float number two: "))
print(f"The average of {fnumOne} and {fnumTwo} is {(fnumOne+fnumTwo)/2}")
print("-------------------Break------------------------")

#practice questions 4
#WAP to input 2 integer numbers a,b and return true if a is greater than b ,If not return false
intA=int(input("Enter value of A: "))
intB=int(input("Enter value of B: "))
print(intA>=intB)

