
def count_uppercase(lst):
  count = 0
  for word in lst:
    for letter in word:
      if letter.isupper():
        count += 1
  return count

