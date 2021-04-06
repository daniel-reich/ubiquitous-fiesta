
def find_even_nums(num):
  vals = [ ]
  for i in range(1, num + 1):
    if i % 2 == 0:
      vals.append(i)
  return vals

