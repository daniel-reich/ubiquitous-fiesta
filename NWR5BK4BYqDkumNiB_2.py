
from functools import reduce
def digital_division(n):
  if n > 0 and n < 10:
    return "Perfect"
  else:
    digits = [int(char) for char in str(n) if char != "0"]
    test1 = list(filter(lambda x: n % x == 0, digits)) == digits
    test2 = n % sum(digits) == 0
    test3 = not "0" in str(n) and n % reduce(lambda x, y: x * y, digits) == 0
    tests = [test1, test2, test3]
    
    if tests.count(True) == 3:
      return "Perfect"
    elif tests.count(True) == 0:
      return "Indivisible"
    else:
      return tests.count(True)

