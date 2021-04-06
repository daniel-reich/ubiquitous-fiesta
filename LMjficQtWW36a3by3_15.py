
def probability(lst, n):
  return (round(((len(list(filter(lambda x: x >= n, lst)))) / len(lst)) * 100, 1))

