
def get_frequencies(lst):
  dic = {}
  for i in set(lst):
    dic[i] = lst.count(i)
  return dic

