
def count_digits(lst, t):
  show = []
  if t == 'odd':
    for num in lst:
      count = 0
      for i in str(num):
        if int(i) % 2:
          count += 1
      show.append(count)
  else:
    for num in lst:
      count = 0
      for i in str(num):
        if int(i) % 2 == 0:
          count += 1
      show.append(count)
  return show

