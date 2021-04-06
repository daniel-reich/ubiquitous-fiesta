
def first_non_repeated_character(txt):
  uniques = [i for i in txt if txt.count(i)==1]
  return uniques[0] if uniques else False

