
def edit_words(lst):
  return [(i[:len(i)//2] + '-' + i[len(i)//2:])[::-1].upper() for i in lst]

