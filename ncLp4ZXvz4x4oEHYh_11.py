
def sum_of_two(a, b, v):
  count = 0
  for number1 in a:
      for number2 in b:
          if (number1 + number2) == v:
              count += 1
          else:
              pass
  if count > 0:
​
      return True
  else:
      return False

