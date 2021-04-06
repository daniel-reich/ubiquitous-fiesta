
def first_non_repeated_character(txt):
  return False if not len(txt) or len(set(txt)) == len(txt)/2 else [i for i in txt if txt.count(i) == 1][0]

