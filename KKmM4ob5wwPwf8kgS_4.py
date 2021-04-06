
def get_frequencies(lst):
  return {item:lst.count(item) for item in set(lst)}

