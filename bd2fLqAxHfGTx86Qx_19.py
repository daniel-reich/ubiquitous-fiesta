
def can_complete(initial, word):
  if ((len(word) == 0) and (len(initial) == 0)):
    return True;
  if ((len(word) == 0) and (len(initial) != 0)):
    return False;
  if (len(initial) == 0):
    return True;
  
  c = initial[0];
  if c in word:
    index = word.index(c);
    return can_complete(initial[1:], word[index+1:])
      
  else:
    return False;

