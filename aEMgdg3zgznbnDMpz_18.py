
def rotated_words(txt):
  return sum(all(char in "HINOSXZWM" for char in word) for word in set(txt.split()))

