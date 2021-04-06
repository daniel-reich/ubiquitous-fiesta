
def get_frequencies(lst):
  final = {}
  for item in lst:
    final[item] = lst.count(item)
  return final

