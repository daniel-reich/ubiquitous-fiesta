
class Calculator:
  # Write methods to add(), subtract(), multiply() and divide()
  
  def __init__(self,num1=0,num2=0):   
    self.num1=num1
    self.num2=num2
  def add(self,num1,num2):
    return num1+num2
  def subtract(self,num1,num2):
    return num1-num2
  def multiply(self,num1,num2):
    return num1*num2
  def divide(self,num1,num2):
    return num1/num2

