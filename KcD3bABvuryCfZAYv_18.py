
def most_frequent_char(lst):
  txt = ''.join(lst)
  m = max(txt.count(c) for c in txt)
  return sorted([c for c in set(txt) if txt.count(c) == m])

