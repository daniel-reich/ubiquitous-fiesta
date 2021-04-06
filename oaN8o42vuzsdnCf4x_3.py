
def best_words(lst):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  score = [1,3,3,2,1,4,2,4,1,8,5,2,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
  key = dict(zip(letters,score))
  points = [sum([key[j] for j in i]) for i in lst]
  return [x for i, x in enumerate(lst) if points[i] == max(points)]

