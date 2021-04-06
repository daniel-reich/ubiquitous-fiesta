
def elasticize(word):
  pivot = len(word)//2
  left = word[:pivot]
  right = word[pivot+(len(word)&1):]
  new_left = new_right = ""
  for i,(x,y) in enumerate(zip(left, right[::-1]), 1):
    new_left += x*i
    new_right = y*i + new_right
  new_center = word[pivot]*((pivot+1) * (len(word)&1))
  return "{}{}{}".format(new_left, new_center, new_right)

