
def join(lst):
  string = lst[0]
  overlap = []
  for i in range(1, len(lst)):
    check = False
    for x in range(len(lst[i-1])):
      temp = lst[i-1][x:]
      if lst[i].startswith(temp):
        overlap.append(len(temp))
        string += lst[i][len(temp):]
        check = True
        break
    if not check:
      string += lst[i]
  if overlap == []:
    overlap = [0]
  return [string, min(overlap)]

