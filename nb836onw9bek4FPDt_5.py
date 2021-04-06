
def count_same_ends(txt):
  import string
  lst = txt.translate(str.maketrans('', '', string.punctuation)).lower().split()
  return len([i for i in lst if i[0] == i[-1] and len(i) > 1])

