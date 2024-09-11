#INTRODUCTION TO OPERATOR

"""
Basically there are 4 types of operators in Python;

1. Assignment Operator
2. Arithmetic Operator
3. Comparison Operator
4. Logical Operator
"""

#Assignment Operator(=)

price = 34

#Arithmetic Operator(+,-,/,//,*,**,%)
"""
+ Plus
- Minus
/ Divide
// Absolute Division
* Multiply
** Exponential
% Modulus
"""

Num1 = 7
Num2 = 3
Add = Num1+Num2
print(f"{Num1} + {Num2} = {Add}")

sub = Num1-Num2
print(f"{Num1} - {Num2} = {sub}")

multiply = Num1*Num2
print(f"{Num1} * {Num2} = {multiply}")

divide = Num1/Num2
print(f"{Num1} / {Num2} = {divide}")

exponential = Num1**Num2
print(f"{Num1} ** {Num2} = {exponential}")

Modulus = Num1%Num2
print(f"{Num1} % {Num2} = {Modulus}")

absolutedivision = Num1//Num2
print(f"{Num1} // {Num2} = {absolutedivision}")

#Comparison Operator
"""
== Equal to (compares two values to check if they are equal. if yes, TRUE. If no, FALSE)
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

"""
height = 10
print (height == 20)

print(height == 10)

print(height > 10)

print(height < 10)

print(height >= 10)

print(height <= 10)

#Logical Operator
"""or
and
not"""

name = "emeka"
age = 34

#AndStatement
print("------------------ AND--------------")

name = "emeka"
age = 34
print(name == "emeka" and age == 34)
print(name == "ebuka" and age == 34)
print(name == "emeka" and age == 24)
print(name == "china" and age == 24)

"""
AND logic can only be true when both conditions are true
"""

print("------------------ OR--------------")
print(name == "emeka" or age == 34)
print(name == "ebuka" or age == 34)
print(name == "emeka" or age == 24)
print(name == "china" or age == 24)

"""
OR logic can only be FALSE when both conditions are FALSE
"""