
def count_digits(lst, t):
  
  class Number:
  
    def __init__(self, val):
      self.v = val
      self.d = [int(i) for i in str(val)]
    
    def return_type(self, t):
      odd = []
      even = []
      for digit in self.d:
        if digit % 2 != 0:
          odd.append(digit)
        else:
          even.append(digit)
      return len(eval(t))
  
  numbers = []
  
  for number in lst:
    numbers.append(Number(number))
  
  count = []
  
  for number in numbers:
    count.append(number.return_type(t))
  
  return count

