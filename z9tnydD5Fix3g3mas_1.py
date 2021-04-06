
def check_pattern(lst, pattern):
  lst = tuple(tuple(item) for item in lst)
  dict1, dict2 = {lst[i]:i for i in range(len(lst))},{l:i for i, l in enumerate(pattern)}
  lst1, lst2 = [dict1[ch] for ch in lst], [dict2[ch] for ch in pattern]
  return lst1 == lst2

