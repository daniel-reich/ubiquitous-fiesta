
def most_frequent_char(lst):
  jn = ''.join(lst)
  cnt = {i:jn.count(i) for i in set(jn)}
  return sorted([j for j, k in cnt.items()  if k == max(cnt.values())])

