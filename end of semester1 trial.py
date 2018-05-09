# Write a script that converts celsius to farnheit.The formula for doing so would be:
# (°C × 9/5) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then
# add 32.The script should take input from STDIN.

			# ANSWER
temp = input("Choose the  temperature to convert: ")
degree = int(temp[:-1])
convertion = temp[-1]

if convertion.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  convert = "Fahrenheit"
elif convertion.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  convert = "Celsius"
else:
  print("Input proper convertion.")
  quit()
print("The temperature in", convert, "is", result, "degrees.")


# Define a class called Person which has at least two methods:getName: to get a persons from console input
# printName: to print the name in upper case.
# Also please include simple test function to test the class methods.

			# ANSWER
class Person:
  
  def __init__(self):
    self.method = ""
    
  def getName(self):
    self.method=input("printName in lowercase:")
    
  def printName(self):
    print (self.method.upper())
    

name = Person()
name.getName()
name.printName()

# Write a program that requests for input from STDIN in a comma separated sequence 
# of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:without,hello,bag,world
# Then, the output should be:bag,hello,without,world

				# ANSWER
input_values = input("Enter csv;")
list_vals = input_values.split(",")
sorted_list = sorted(list_vals)
sorted_values = ','.join(sorted_list)
print (sorted_values)

# "Write a program that prints the numbers from 1 to 100. But for multiples of three print 
# “Fizz” instead of the number and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”."

				# ANSWER
def fizzbuzz():
  for i in range(1,101):
    print("Fizz" * (i%3==0) + "Buzz" * (i%5==0) or i)
    
print (fizzbuzz())
   