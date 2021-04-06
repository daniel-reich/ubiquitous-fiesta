
def best_words(lst):
  return [x for x in lst if score(x) == max(score(x) for x in lst)]
​
def score(word):
  points = {
  1  : 'aeinorstu',
  2  : 'dgl',
  3  : 'bcmp',
  4  : 'fhvwy',
  5  : 'k',
  8  : 'jx',
  10 : 'qz'}
  return sum(x for x in points.keys() for y in word if y in points[x])

