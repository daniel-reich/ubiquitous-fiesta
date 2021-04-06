
vows = 'aeiou'
​
def get_vowel_substrings (txt):
  n = []
  i = 0
  for t in txt:
    if t in vows: n.append (i)
    i += 1
  a = [(i,j) for i in n for j in n if j >= i]
  return (sorted (set([txt[i[0]:i[1]+1] for i in a])))
​
def get_consonant_substrings (txt):
  n = []
  i = 0
  for t in txt:
    if t not in vows: n.append (i)
    i += 1
  a = [(i,j) for i in n for j in n if j >= i]
  return (sorted (set([txt[i[0]:i[1]+1] for i in a])))

