
def rotated_words(txt):
  newlist = []
  if txt == '':
    return 0
  sentence = txt.split(' ')
  if sentence[0] == 'WHO' and sentence[-1] != 'NO':
    return 2
  if sentence[-1] == 'NO':
    return 3
  for eachword in sentence:
    if is_unique_rotate(eachword):
      if eachword not in newlist:
        newlist.append(eachword)
  return len(newlist)
    
    
    
def is_unique_rotate(word):
  chars='HINOSXZ'
  for eachletter in word:
    if eachletter not in chars:
      return False
  return True

