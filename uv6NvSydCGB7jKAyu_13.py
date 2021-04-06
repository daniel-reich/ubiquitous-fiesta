
def is_parsel_tongue(s):
  lst = s.split(" ")
  for x in lst:
    count = 0
    for y in range(len(x)):
      if x[y] == 's' or x[y] == 'S':
        count += 1
      else:
        if count == 1:
          return False
        count = 0
  return True

