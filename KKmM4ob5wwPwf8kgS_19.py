
def get_frequencies(lst):
  return {i : lst.count(i) for i in list(dict.fromkeys(lst))}

