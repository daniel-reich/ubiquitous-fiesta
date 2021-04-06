
key = (
  ('a','b','c','d','e'),
  ('f','g','h','i','k'),
  ('l','m','n','o','p'),
  ('q','r','s','t','u'),
  ('v','w','x','y','z'))
​
def bifid(txt):
  if all(ch.islower() for ch in txt):
    lst = []
    for ch in txt:
      x, y = get_index(ch)
      lst.append(x)
      lst.append(y)
    mid = len(lst)//2
    top, bottom = lst[:mid], lst[mid:]
    lst = [(top[i],bottom[i]) for i in range(len(top))]
    return ''.join(get_letter(i) for i in lst)
    
  else:
    lst = [get_index(ch) for ch in txt.lower() if ch.isalpha()]
    lst = [i[0] for i in lst] + [i[1] for i in lst]
    return ''.join(get_letter((lst[i],lst[i+1])) for i in range(0,len(lst)-1,2))
  
def get_index(c):
  global key
  for i, x in enumerate(key):
    if c in x:
      return i,x.index(c)
​
def get_letter(t):
  global key
  r, c = t
  return key[r][c]

