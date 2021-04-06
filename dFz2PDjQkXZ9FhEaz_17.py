
def letter_check(lst):
  lst1 = [i.lower() for i in lst]
  return all([i in lst1[0] for i in lst1[1]])

