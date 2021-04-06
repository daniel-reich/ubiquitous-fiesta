
def digit_distance(num1, num2):
  return sum([abs(int(str(num1)[i]) - int(str(num2)[i])) for i in range(len(str(num1)))])

