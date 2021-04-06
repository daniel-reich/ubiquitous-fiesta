
def replace_the(txt):
  r=[] ; txt = txt.split()
  for i in range(len(txt)-1):
    if txt[i]!='the': r.append(txt[i])
    elif txt[i+1][0] in 'aeiou': r.append('an')
    else: r.append('a')
  r.append(txt[-1])
  return ' '.join(r)

