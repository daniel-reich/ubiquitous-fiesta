
def count_uppercase(lst):
  return sum(i.isupper() for word in lst for i in word)

