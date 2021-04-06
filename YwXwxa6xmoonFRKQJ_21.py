
def josephus(n):                          # Josephus Survivor
  if not n: return False
  josephus_list = list(range(1, n+1))
  index = 1                           # Simply because indexes start at 0
  while len(josephus_list)>1:
    index %= len(josephus_list)
    josephus_list.pop(index)
    index += 1
  return list(range(1, n+1)).index(josephus_list[0])

