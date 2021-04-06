
def word_nest(word, s):
​
  count = -1
​
  while s:
    s = s.replace(word, '')
    count += 1
​
  return count

