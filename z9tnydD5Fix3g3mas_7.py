
def check_pattern(lst, pattern):
  lst = [lst_to_int(x) for x in lst]
  match = dict(zip(pattern, lst))
  if len(match) != len(set(match.values())):
    return False
  
  return all(True if match[x] == lst[i] else False for i, x in enumerate(pattern))
​
def lst_to_int(lst):
  return int("".join([str(x) for x in lst]))

