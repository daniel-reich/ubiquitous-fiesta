
def count_words(txt):
  count = 1
  for letter in txt:
    if letter == " ":
      count+=1
  return count

