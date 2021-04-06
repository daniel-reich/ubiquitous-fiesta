
def digit_distance(num1, num2):
  sum = 0
  num1 = str(num1)
  num2 = str(num2)
  for i in range (len(num1)):
    sum += abs(int(num1[i])-int(num2[i]))
  return sum

