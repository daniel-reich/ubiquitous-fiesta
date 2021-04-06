
def plus(n1, n2):
  return n1 + n2
  
def minus(n1, n2):
  return n1 - n2
  
def dict_key_from_value(dict, value):
  return list(dict.keys())[list(dict.values()).index(value)]
​
def wordedMath(equ):
  numbers = {
    "zero": 0,
    "one": 1,
    "two": 2
  }
  operations = {
    "plus": plus,
    "minus": minus
  }
  n1, op, n2 = equ.lower().split()
  return dict_key_from_value(numbers, operations[op](numbers[n1], numbers[n2])).title()

