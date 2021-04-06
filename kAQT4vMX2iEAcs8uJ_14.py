
def longest_7segment_word(lst):
  qualifies = []
  for word in lst:
    nogood = False
    for letter in word:
      if letter in ['k', 'v', 'm', 'w', 'x']:
        nogood = True
    if nogood:
      continue
    qualifies.append(word)
  if qualifies:
    temp = list(map(len, qualifies))
    return qualifies[temp.index(max(temp))]
  else:
    return ""

