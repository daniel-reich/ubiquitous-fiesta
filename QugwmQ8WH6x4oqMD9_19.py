
def count_identical_lists(*args):
  x = [str(i) for i in args]
  return [len(x) - len(set(x))+1, 0][len(x) == len(set(x))]

