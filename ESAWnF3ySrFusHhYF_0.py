
def edit_words(lst):
  return [(x[:len(x)//2]+'-'+x[len(x)//2:])[::-1].upper() for x in lst]

