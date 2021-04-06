
def can_complete(initial, word):
  letters = list(initial);
  for i in range(len(letters) - 1):
    x = letters[i];
    if word.find(x) != -1:
      if word.find(x) > word.find(letters[i+1]) or word.count(x) < initial.count(x):
        return False;
    else: return False;
  return True;

