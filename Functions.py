#functions

def hello():
  name = str(input("Enter your name: "))
  if name:
    print ("Hello " + str(name))
  else:
    print("Hello World")
hello()

#welcome

def welcome_student(name):
  welcome_str = "Hi {} welcome to Akirachix"
  return welcome_str.format(name)
name = input("Enter student name:")
print(welcome_student(name))
print(welcome_student("ivy"))
print(welcome_student("Felicia"))


#Area

def area_triangle(base,height):
  return 0.5*base*height
  
def area_circle(radius):
  return 3.14*radius*radius
  
def area_rectangle(base,height):
  return base*height
  
height,base, radius = 50,70,30

print ("Area of triangle = {}".format(area_triangle(base,height)))
print ("Area of circle = {}".format(area_circle(radius)))
print ("Area of rectangle = {}".format(area_rectangle(base,height)))

#parameters

def show_parameters (*args):
  for i in args:
    print(i)
    
show_parameters("Judith", "Ivy", "Fatma")

#TOTAL PARAMS

def total_parameters(*args):
  for i in args(10):
      print("total_parameters")
total_parameters(5,6)
  

  #params

  def total_params(*args):
  total = 0
  for i in args:
    total=total+i
  return total
print(total_params(1,2,3,4,7))

#args

def welcome_student(name):
  welcome_str = "Hi {}, Welcome to Akirachix"
  return welcome_str.format(name)

def welcome_all(*args):
  for student in args:
    print(welcome_student(student))
welcome_all("jane", "Judith", "Cate", "vickey")

#tax

# income = ("what is your current income");

# def tax_paid(income):
#   return 0.3 * income
# print (tax_paid)




def tax_paid(income):
  return 0.3 * income
income=3200
print ("what is the current income?".format(tax_paid(income)))

#tax_1

# income = input("what is your current income;")
# tax = 0.3 * int(income)
# print ("the tax is {}" . format(tax))


def calculate_tax(income):
  return float(income)*0.3
  
income = input("what is your income;")
tax = calculate_tax(income)
print(tax)