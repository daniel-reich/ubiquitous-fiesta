
def count_repetitions(lst):
  a = sorted([[i, lst.count(i)] for i in set(lst)], key=lambda x: x[1])
  return {i[0]:i[1] for i in a[::-1]}

