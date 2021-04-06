
def ascii_sort(lst):
  a, b = lst
  a_score = sum(ord(ch) for ch in a)
  b_score = sum(ord(ch) for ch in b)
  if a_score < b_score :
    return a
  else:
    return b

