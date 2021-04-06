
def digit_distance(num1, num2):
  return sum(abs(int(n1)-int(n2)) for n1,n2 in zip(str(num1),str(num2)));

