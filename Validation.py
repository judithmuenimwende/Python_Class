  #Rectangle

class Rectangle:
  def __init__(self, length, width):
    
    self.length = length
    self.width = width
    self.validateDimension()
    
  
  def validateDimension(self):
  
    try:
      self.width = float(self.width)
      self.length = float(self.length)
    except ValueError:
      raise ValueError("Dimensions can not be converted to integer")
  
  
     
  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2*(self.length + self.width)
 
invalid = Rectangle("6","5")
print(invalid.area())

    #Tax_payer

    class TaxPayer:
  income = 0
  name = "Jane Doe"
  def __init__(self,name,income):
    self.income = income
    self.name = name
    self.validateIncome()
    self.validateName()
    self.validateMinimum()
    
  def validateIncome(self):
    if self.income.isnumeric() == False:
      raise ValueError("The income {} is not numeric".format(self.income))
  
  def validateName(self):
    if self.name.isnumeric():
      raise ValueError("The name {} is not a string".format(self.name))
  
  def validateMinimum(self):
    if float(self.income) < 100001:
      raise ValueError("Below minimum wage")
      
  def calculate_tax(self):
    return float(self.income) * 0.3


income = input("What is your income")
name = input("What is your name?")
employee = TaxPayer(name,income)
print(employee.calculate_tax())