
def count_uppercase(lst):
  return sum(j.isupper() for i in lst for j in i)

