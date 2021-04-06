
def censor(s):
  lst = s.split()
  new_list = []
  for word in lst:
    if len(word) > 4:
      new_list.append((word.replace(word, len(word) * '*')))
    else:
      new_list.append(word)
​
  return ' '.join(new_list)

