
def count_digits(lst, t):
  for j in range(len(lst)):
    i = 0
    for j1 in range(len(str(lst[j]))):
      if t == 'odd':
        if int(str(lst[j])[j1]) % 2 != 0:
          i += 1
      elif t == 'even':
        if int(str(lst[j])[j1]) % 2 == 0:
          i += 1
    lst[j] = i
  return lst

