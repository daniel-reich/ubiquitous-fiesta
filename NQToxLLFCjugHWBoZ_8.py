
def sort_by_character(lst, n):
  l = []
  copy = lst
  for j in range(len(lst)):
    early = copy[0]
    for i in range(len(copy)):
      if copy[i][n-1] < early[n-1]:
        early = copy[i]
    l.append(early)
    copy.remove(early)
  return(l)

