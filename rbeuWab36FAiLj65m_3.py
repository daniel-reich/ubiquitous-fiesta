
def grouping(w):
  groups = {}
  for word in w:
    n_up = 0
    for char in word:
      if char.isupper():
        n_up+=1
    if n_up not in groups.keys():
      groups[n_up] = []
    groups[n_up].append(word)
  for key in groups.keys():
    groups[key] = sorted(groups[key], key = str.casefold) 
  return groups

