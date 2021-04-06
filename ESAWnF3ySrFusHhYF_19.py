
def edit_words(lst):
  for n, word in enumerate(lst):
    rev = word[::-1].upper()
    ndx = len(word)//2 + len(word)%2
    lst[n] = rev[:ndx] + '-' + rev[ndx:]
  return lst

