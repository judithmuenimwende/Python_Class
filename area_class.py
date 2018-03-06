radius= input("what is the radius:")
area= 3.142 * int(radius) * int(radius)
perimeter= 3.142 * 2 * int(radius)
print("The area is {}".format(area))
print("The perimeter is {}".format(perimeter))


# student_strings

student= ["irene", "Judith", "Assumpter"]
welcome_str= "welcome Ms {} to Akirachix"
print (welcome_str.format(student[0]))
print (welcome_str.format(student[1]))
print (welcome_str.format(student[2]))
student.append("yvonne")
student.append("Jane")
print (welcome_str.format(student[3]))
print (welcome_str.format(student[4]))

#using_for

students= ["irene", "Judith", "Laureen"]
welcome_str="Ms {} you are a good student"
for student in students:
 print (welcome_str.format(student))

 #for_range

 students = ["irene", "Judith", "Laureen"]
for i in range(3):
  print("student number {} is {}".format(i , students[i]))

  #welcome_string

  name= input("what is your name:")
str_format= "welcome {} to Akirachix"
print(str_format.format(name))

#range_print

numbers= range (5)
print(numbers[0])
print(numbers[1])
print(numbers[2])