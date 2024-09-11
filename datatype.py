#Python Datatypes are grouped into 2: primitive datatype and data collation.... Examples of primitive: string, integer, boolean, float
#examples of data collation: list, tuple, dictionary, set
#String
city = "London"
print(type(city))

school = 'gskills'
print(type(school))

description = """python is all purpose programming language"""
print(type(description))

#anything inside "" is a string

#Integer

age = 34
print(type(age))

#integer is a whole number

price = 50.55
print(type(price))

#Boolean

is_learning = True
print(type(is_learning))

is_sleeping = False
print(type(is_sleeping))

#DataCollation

#list
friends = []            #this is how to create a list in python (empty list)
print(type(friends))

friends = ["peter", "john", "james", "Paul"] #adding values to friends list
print(friends)
"""
Note: the list can hold any datatype example (string, integer, tuple, dictionary, set etc)
"""

#Tuple
family = () #How to create a tuple
print(type(family)) #how to check a data type
family =("john", "Paul", "emenike") #how to insert a value
print(family) #how to print the values
#dictionary

student = {} #hOW TO CREATE A DICTIONARY
print(type(student)) #how to check the datatype

student = {
    "name":"emeka",
    "age": 36,
    "course": "micobiology",
    "school": "egbezaga"
} #how to insert a value to a dictionary
print(student)
#dictionary is a value pair datatype. leftside is the key while the right side is the value. the key and value is called ITEM...