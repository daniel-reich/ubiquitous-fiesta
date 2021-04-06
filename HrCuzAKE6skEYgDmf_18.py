
def pairs(lst):
  result, i = [], 0
  while len(result) < len(lst) / 2:
    result.append([lst[i], lst[-(1 + i)]])
    i += 1
  return result

