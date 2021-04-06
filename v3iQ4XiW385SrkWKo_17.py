
def final_result(lst):
  lst.append("magic")
  found = True
  while found:
    if len(lst) == 1:
      break
    i = 0
    found = False
    while True:
      if lst[i] == lst[i+1]:
        found = True
        for j in range(i+1, len(lst)):
          if lst[j] != lst[i]:
            break
        for _ in range(j-i):
          lst.pop(i)
        break
      i = i + 1
      if i > len(lst)-2: break
  
  lst.pop(-1)
  return lst

