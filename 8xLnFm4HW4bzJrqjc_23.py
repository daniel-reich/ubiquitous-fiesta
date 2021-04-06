
def digit_distance(num1, num2):
  sum = 0
  for i in range(len(str(num1))):
    sum = sum + abs(int((str(num1)[i])) - int((str(num2))[i]))
  return sum

