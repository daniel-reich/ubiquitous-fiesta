
def edit_words(lst):
  return [hyphenate(x).upper()[::-1] for x in lst]
    
    
    
def hyphenate(word):
  if len(word) == 0:
    return '-'
  middle = len(word) // 2
  word = list(word)
  newlist = []
  for i in range(len(word)):
    if i == middle:
      newlist.append('-')
      newlist.append(word[i])
    else:
      newlist.append(word[i])
  return ''.join(newlist)

