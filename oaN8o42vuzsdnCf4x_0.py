
def best_words(lst):
  lett = 'abcdefghijklmnopqrstuvwxyz'
  vals = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10)
  d = dict(zip(lett, vals))
  scores = [sum(d[i] for i in word) for word in lst]
  return [lst[idx] for idx, i in enumerate(scores) if i == max(scores)]

