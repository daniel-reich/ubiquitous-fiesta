
def group(lst, size):
  n = len(lst)//size
  if len(lst)%size == 0:
    grouped = [[] for i in range(n)]
    for i in range(len(lst)):
      grouped[i%n].append(lst[i])
    return grouped
  else:
    grouped = [[] for i in range(n+1)]
    for i in range(len(lst)):
      grouped[i%(n+1)].append(lst[i])
    return grouped

