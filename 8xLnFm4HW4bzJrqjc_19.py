
def digit_distance(num1, num2):
  lst1 = [int(d) for d in str(num1)]
  lst2 = [int(d) for d in str(num2)]
  return abs(sum([i[0] - i[1] for i in list(zip(lst1, lst2))]))

