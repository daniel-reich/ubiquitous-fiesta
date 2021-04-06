
def playfair(txt, key):
  encoded = False if ' ' in txt else True
  polybius = get_deranged_polybius(key)
  txt = adjust_doubles(txt)
​
  if not encoded:
    return encode_decode(polybius,txt)
  else:
    return encode_decode(polybius,txt,decode=True)
​
def encode_decode(polybius,txt,decode=False):
  adj = -1 if decode else 1
  res = ''
  for a, b in txt:
    a = get_index(polybius,a)
    b = get_index(polybius,b)
​
    if a[0] == b[0]:
      ax,ay = [a[0],(a[1]+adj)%5]
      bx,by = [b[0],(b[1]+adj)%5]
    elif a[1] == b[1]:
      ax,ay = [(a[0]+adj)%5,a[1]]
      bx,by = [(b[0]+adj)%5,b[1]]
    else:
      ax,ay = [a[0],b[1]]
      bx,by = [b[0],a[1]]
​
    res += polybius[ax][ay] + polybius[bx][by]
  return res
​
def get_index(polybius,letter):
  for i, j in enumerate(polybius):
    if letter in j:
      return (i,j.index(letter)) 
​
def adjust_doubles(txt):
  txt = [i for i in txt.upper() if i.isalpha()]
  txt = [''.join(txt[i:i+2]) for i in range(0,len(txt),2)]
​
  while any(len(set(i))==1 and len(i)==2 for i in txt):
    for i in range(len(txt)):
      if len(set(txt[i]))==1:
        txt[i] = txt[i][0] + 'X' + txt[i][1]
        break
    txt = ''.join(i for i in txt)
    txt = [''.join(txt[i:i+2]) for i in range(0,len(txt),2)]
  if len(txt[-1]) != 2:
    txt[-1] += 'X'
  return txt
​
def get_deranged_polybius(key):
  res = []
  for ch in key.upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
    if ch not in res:
      res.append(ch)
  return [res[i:i+5] for i in range(0,25,5)]

