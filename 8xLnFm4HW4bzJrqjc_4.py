
def digit_distance(num1, num2):
  return sum(abs(int(i)-int(j)) for i,j in zip(str(num1), str(num2)))

