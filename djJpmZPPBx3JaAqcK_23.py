
def maya_number(n):
  
  class Base:
​
    def __init__(self, base):
      self.b = base
    
    def convert(self, b10num):
​
      divisors = [1]
      exp = 1
      while max(divisors) <= b10num:
        divisors.append(self.b ** exp)
        exp += 1
      
      divisors = list(reversed(divisors))[1:]
​
      digits = []
​
      for divisor in divisors:
        digit = int(b10num / divisor)
        digits.append(digit)
        b10num = b10num % divisor
      
      return digits
  def convert_to_maya(number):
    ints = list(sorted(range(0, 20)))
    maya = '@ o oo ooo oooo - o- oo- ooo- oooo- -- o-- oo-- ooo-- oooo-- --- o--- oo--- ooo--- oooo---'.split()
​
    int_to_maya = {}
​
    for n in range(20):
      int_to_maya[ints[n]] = maya[n]
    
    mayan_digits = []
​
    for digit in number:
      mayan_digits.append(int_to_maya[digit])
    
    return mayan_digits
​
  if n == 0:
    return ['@']
  
  b = Base(20)
  converted = b.convert(n)
​
  return convert_to_maya(converted)

