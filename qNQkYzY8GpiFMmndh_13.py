
def join(lst):
  res, minimum = lst.pop(0), 0
​
  for word in lst:
    i = min(len(res),len(word))
    while i > 0:
      if res[-i:] != word[:i]:
        i -= 1
      else:
        res += word[i:]
        if not minimum or i < minimum:
          minimum = i
        break
    if i == 0:
      res += word
  return [res,minimum]

