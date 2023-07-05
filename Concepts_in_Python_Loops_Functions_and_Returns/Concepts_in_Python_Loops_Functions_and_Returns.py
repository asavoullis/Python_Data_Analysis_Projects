"""
Concepts in Python: Loops Functions and Returns

Course Objectives:

Understand and implement loops in Python.
Understand and implement functions in Python.
Understand and implement return statements in Python.


By the end of this course, you will be able to:

By the end of Task 1,  you will be able to demonstrate a while loop.                                                         
By the end of Task 2,  you will be able to create a for and else loop.
By the end of Task 3,  you will be able to implement loop control statements.
By the end of Task 4,  you will be able to create a nested loop.
By the end of Task 5,  you will be able to create and demonstrate Python functions.
By the end of Task 6,  you will be able to develop return statements with one value and multiple values


Project Structure:

Task 1: While loops
Task 2: For loop and else clause
Task 3: Loop control statements
Task 4: Nested loops
Task 5: Functions in Python
Task 6: Return statements

"""

# Example 1:
"""
In Python, the else clause in a for loop is executed only if the loop completes all its iterations without encountering a break statement. 
If a break statement is encountered, the else clause is skipped, and the code proceeds to execute the code following the loop.
"""
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    print(num)
    if num == 7:
        break
    print("Inside for loop")
else:
    print("Outside for loop")

print("")
# Example 2:
"""
When num is 5, the condition num == 5 is met, and the break statement is executed, causing the loop to terminate early. 
Since the loop did not complete all iterations without encountering a break, the else clause is skipped, and "Outside for loop" will not be printed.
"""
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    print(num)
    if num == 5:
        break
    print("Inside for loop")
else:
    print("Outside for loop")

print("")
# Example 3:
cars = ["Audi", "VW", "Jaguar", "Mini"]
for car in cars:
    if car == 'Jaguar':
        break
    print(car)

print("")
# Example 4:
cars = ["Audi", "VW", "Jaguar", "Mini"]
for car in cars:
    if car == 'Jaguar':
        continue
    print(car)

print("")
# Example 5:
counter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for count in counter:
    if count == 6:
        print("Number needs to be skipped")
        continue
    print(count)

print("")
# Example 6:
counter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for count in counter:
    # If its odd skip it
    if count %2:
        pass
    else:
        print(count)

print("")
# Example 7:
numbers2 = [1,2,3]
letters = ['a','b','c']
for num in numbers2:
    print(num)
    for letter in letters:
        print(letter)

print("")
# Example 8:
# var = 1 
# while var == 1:
#     print(var)

print("")
# Example 9:
number = 1
while number < 5:
    print(number)
    number += 1

print("")
# Example 10:
counter2 = 26
while counter2 > 15:
    print(counter2)
    counter2 -= 2
print("While loop has ended")

print("")
# Example 11:
def print_name(name):
    print("My name is : "+ name)
print_name("Emma")

print("")
# Example 12:
def print_name2(fname, lname):
    print("My name is : "+fname+" "+ lname)
print_name2("Emma", "Martin")

print("")
# Example 13:
def print_name2(fname, lname, age):
    print("My name is : "+fname+" "+lname+"and my age is : "+str(age))
print_name2("Emma", "Martin", 34)

print("")
# Example 14:
def print_name3(fname = "Emma"):
    print("My name is : "+fname)
print_name3("Emma")

print("")
# Example 15:
def mutliply(num1, num2):
    return num1 * num2
result = mutliply(2,3)
print("Results = {}".format(result))


print("")
# Example 16:
def greeting(name):
    return "Hello "+name
result2 = greeting("Emma ")
print(result2)