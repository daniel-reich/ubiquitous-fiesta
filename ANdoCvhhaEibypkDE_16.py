
def pairs(word):
  p = []
  while len(word) > 1:
    p.append(word[0]+word[-1])
    word = word[1:-1]
  if word:
    p.append(word)
  return p
def closing_in_sum(n):
  n = list(map(int, pairs(str(n))))
  return sum(n)

