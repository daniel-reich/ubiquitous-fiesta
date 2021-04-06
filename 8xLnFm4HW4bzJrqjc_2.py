
def digit_distance(num1, num2):
  return sum([abs(int(x)-int(y)) for (x,y) in zip(str(num1),str(num2))])

