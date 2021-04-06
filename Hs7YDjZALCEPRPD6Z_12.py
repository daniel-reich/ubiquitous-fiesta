
def count_uppercase(lst):
  return sum(sum([1 for letter in word if letter.isupper()]) for word in lst)

