
def remix(txt, lst):
 new = [0]*len(txt)
 x = 0
 while x < len(txt):
  new[lst[x]] = txt[x]
  x += 1
 return ''.join(new)

