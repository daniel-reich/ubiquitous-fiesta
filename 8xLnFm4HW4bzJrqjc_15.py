
def digit_distance(num1, num2):
  return sum(abs(int(a)-int(b)) for a,b in zip(str(num1),str(num2)))

