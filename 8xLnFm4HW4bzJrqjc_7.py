
def digit_distance(num1, num2):
  num1 = [int(i) for i in str(num1)]
  num2 = [int(i) for i in str(num2)]
  return abs(sum([num1[i] - num2[i] for i in range(len(num1))]))

