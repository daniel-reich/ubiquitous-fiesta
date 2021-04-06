
def count_uppercase(lst):
  return sum(letter.isupper()  for word in lst for letter in word)

