text=input("Enter your name: ")
textInt= int(input("Enter your age: "))
textFloat= float(input("Enter any floating value: "))

# StudentDetails=text,textInt,textFloat
# print("The details of student are:"+ StudentDetails)

info= "My name is {name} and age is {age}".format(name=text,age=textInt)
print(info)

