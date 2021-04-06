
def count_uppercase(lst):
  return sum(1 for letter in "".join(lst) if letter.isupper())

