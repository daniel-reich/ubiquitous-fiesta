
def last_vowel(word):
  for i in word[::-1]:
    if i.lower() in 'aeiou':
      return i.lower()
​
def common_last_vowel(txt):
  words = txt.split(' ')
  last = {}
  for word in words:
    lv = last_vowel(word)
    if lv not in last:
      last[lv] = 1
    else:
      last[lv] += 1
  counts = [last[i] for i in last]
  winner = [i for i in last if last[i] == max(counts)]
  return winner[0]

