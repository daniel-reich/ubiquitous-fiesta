
def group_seats(lst, n):
  counter = 0
  for row in lst:
    k = 0
    while k < len(row):
      if row[k] == 0:
        count = 0
        j = k
        while j < len(row) and row[j] == 0:
          count += 1
          j += 1
        if count >= n:
          counter += (count + 1- n)
        k = j
      else:
        k += 1
  return counter

