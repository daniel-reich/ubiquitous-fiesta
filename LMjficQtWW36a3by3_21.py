
def probability(lst, n):
  favorables = 0
  for i in range(len(lst)):
    if(lst[i] >= n):
      favorables += 1
  return round(((favorables / len(lst))*100), 1)

