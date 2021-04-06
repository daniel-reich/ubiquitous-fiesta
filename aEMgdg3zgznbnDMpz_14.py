
def f(word):
  for letter in word:
    if letter.lower() not in 'hinosxzwm':
      return False
  return True
​
def rotated_words(txt):
  words = list(set(txt.split()))
  count = 0
  for word in words:
    if f(word):
      count += 1
  return count

