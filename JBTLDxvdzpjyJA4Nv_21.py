
import re
​
def super_reduced_string(txt):
  res = ''
  done = False
  while not done:
    i = 0
    # print(txt, res)
    while True:
      if i > len(txt) - 1:
        break
      if i == len(txt) - 1 or (txt[i] != txt[i+1]):
        res += txt[i]
        i += 1
      else:
        i += 2
    if res == txt:
      done = True
    else:
      txt = res
      res = ''
  if not res:
    res='Empty String'
  return res

