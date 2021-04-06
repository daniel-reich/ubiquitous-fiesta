
def count_claps(t):
  count = 0
  for i in range(len(t)):
    if t[i] == 'C':
      count += 1
  return count

