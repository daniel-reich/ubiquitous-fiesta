
def matchingWords(string, lst):
  return [w for w in lst if string.startswith(w)]
  
def cleave(string, lst):
  possibles = [(string, [])] # elements are (remaining string, [words])
  while len(possibles) > 0:
    potential = possibles.pop(0)
    matches = matchingWords(potential[0], lst)
    for m in matches:
      wds = potential[1].copy()
      wds.append(m)
      remaining = potential[0][len(m):]
      if len(remaining) == 0:
        return ' '.join(wds)
      possibles.append((remaining, wds))
      print(possibles)
  return 'Cleaving stalled: Word not found'

