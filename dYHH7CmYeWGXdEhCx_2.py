
def word_builder(letters, positions):
  l=[None]*max(positions)
  l.append(letters[positions.index(min(positions))])
  for i,j in zip(letters,positions):
      if l[j] != i: 
          l[j]=i       
  return ''.join(l)

