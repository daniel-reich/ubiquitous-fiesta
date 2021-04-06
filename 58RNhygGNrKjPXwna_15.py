
def longest_nonrepeating_substring(txt):
  x = ''
  for i in range(len(txt)):
      y,f = '',False
      for j in txt[i:]:
          if j not in y and f==False:
              y += j
          else:
              f = True
      if len(x)<len(y):
          x = y
  return x

