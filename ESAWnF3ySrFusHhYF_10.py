
def edit_words(lst):
  return [(w[0:len(w)//2] + '-' + w[len(w)//2:])[::-1].upper() for w in lst]

