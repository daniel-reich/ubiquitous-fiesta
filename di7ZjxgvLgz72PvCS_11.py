
def validate_swaps(lst, txt):
  result = []
  for i in lst:
    if sorted(i) == sorted(txt):
      diff = 0
      for j in range(len(i)):
        if i[j] != txt[j]:
          diff += 1
      if diff == 2: result.append(True)
      else: result.append(False)
    else: result.append(False)
  return result

