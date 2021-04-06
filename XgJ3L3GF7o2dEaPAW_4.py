
def shared_letters(a, b):
  return ''.join(sorted(intersect(split(a.lower()), split(b.lower()))))
​
def intersect(l1, l2):
  return list(set([x for x in l1 if x in l2]))
​
def split(w):
  return [c for c in w]

