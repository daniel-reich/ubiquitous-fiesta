
def amplify(num):
  lst = []
  for value in range(1, num+1):
    if value % 4 == 0:
      lst.append(value*10)
    else:
      lst.append(value)
  return lst

