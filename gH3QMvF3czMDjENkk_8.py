
def remove_letters(letters, word):
  l = []
  k = []
  for i in letters:
    if i in word:
      if i not in k:
        k.append(i)
      else:
        if word.count(i) == k.count(i):
          l.append(i)
        else:
          k.append(i)
    else:
      if i not in l:
        l.append(i)
​
  return l

