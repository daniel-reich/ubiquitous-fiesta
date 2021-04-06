
def digit_distance(num1, num2):
  l = len(str(num1))
  s1 = str(num1)
  s2 = str(num2)
  
  total = 0
  for i in range(l):
    total += abs(int(s1[i])-int(s2[i]))
    
  return total

