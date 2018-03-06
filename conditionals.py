#in-conditionals

value_1= input("Enter value 1:")
value_2= input("Enter value 2:")
if value_1 > value_2:
  print("value 1 is greater")
if value_2 > value_1:
  print("value 2 is greater")

  #if,elif,else conditionals

  device=input("Enter device:")
if device=="Feature":
  print("This is a Feature")
elif device=="android":
  print("This is an android")
else:
  print("unknown device")

  #in_class

  marks= input("what did student score")
marks= int(marks)
if marks > 90:
  print("A")
elif marks > 70:
  print("B")
elif marks > 80:
  print("C")
else:
  print("D")

  #grades

  marks= input("what did the student score")
marks= int(marks)
if marks>90:
  print("A")
elif marks>70:
  print("B")
elif marks>50:
  print("C")
else:
  print("D")