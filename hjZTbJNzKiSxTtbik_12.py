
def sort_by_string(lst, txt):
  newSort = []
  for letter in txt:
    for word in lst:
      if word[0] == letter:
        newSort.append(word)
  return newSort

