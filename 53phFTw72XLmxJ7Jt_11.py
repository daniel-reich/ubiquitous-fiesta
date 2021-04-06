
def marathon_distance(d):
  total = 0
  for num in d:
    print (abs(num))
    total = total + abs(num)
    print (total)
  if total == 25:
    return True
  else:
    return False

