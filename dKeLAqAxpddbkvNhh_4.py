
def group_seats(lst, n):
  num = 0
  for row in lst:
    for i in range(len(row)-n + 1):
      if row[i] == 0 and all(row[i + j] == 0 for j in range(n)):
        num += 1
  return num

