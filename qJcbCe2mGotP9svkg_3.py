
def num_to_google(lst):
  d={'1':'g', '2':'o', '3':'l', '4':'e'}
  lst=[str(x) for x in lst]
  s=''
  for x in lst:
    if '9' in x:
      break
    for y in x:
      if y in d:
        s+=d[y]
      else:
        if y=='5':
          s=s.upper()
        elif y=='6':
          s+='.'
        elif y=='7':
          s=s[0].upper()+s[1:]
        elif y=='8':
          s=s[::-1]
        elif y=='0':
          s=s[:-1]+s[-1]*int(x[x.index('0')+1:])
          break
  return s

