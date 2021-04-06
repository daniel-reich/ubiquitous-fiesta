
def digit_distance(num1, num2):
  num3 = str(abs(num1 - num2))
  return sum(int(i) for i in num3)

