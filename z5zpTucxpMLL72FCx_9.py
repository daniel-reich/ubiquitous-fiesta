
def grab_city(txt):
  seen,t,l = 0,'',len(txt)-1
  while seen < 1:
    if txt[l].isalpha() or txt[l] == ' ':
      t += txt[l]
    if txt[l] == '[':
      seen += 1
    l-=1
  return t[::-1]

