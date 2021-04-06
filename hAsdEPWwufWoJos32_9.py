
def no_yelling(phrase):
  lst = phrase.split()
  last = lst[-1]
​
  c1 = last.count('!')
  if c1 > 0:
    last = last.replace(c1*'!', '!')
​
  c2 = last.count('?')
  if c2 > 0:
    last = last.replace(c2*'?', '?')
​
  lst[-1] = last
  return ' '.join(lst)

