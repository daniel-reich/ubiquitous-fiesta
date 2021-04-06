
def digit_distance(num1, num2):
  return abs(sum([int(i[0])-int(i[1]) for i in zip(str(num1),str(num2))]))

