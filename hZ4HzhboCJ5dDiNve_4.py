
def special_reverse_string(txt):
  s = txt.replace(' ','')[::-1].lower()
  i=0 ; r=''
  for j in txt:
    if j==' ': r+=j
    else:
      if (not j.isalpha()) or j.islower(): r+=s[i]
      else: r+=s[i].upper()
      i+=1
  return r

