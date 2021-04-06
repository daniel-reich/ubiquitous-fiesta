
def count_repetitions(lst):
  return {i:lst.count(i) for i in set(lst)}

