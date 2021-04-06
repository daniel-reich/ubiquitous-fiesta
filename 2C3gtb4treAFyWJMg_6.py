
def polybius(text):
  alpha = "abcdefghiklmnopqrstuvwxyz"
  m=''
  if text[0].isalpha():
    t=text.lower().replace('j','i')
    for i in t:
      if i.isalpha():
        x = alpha.index(i)
        m+=str(x//5 + 1) + str(x%5 +1)
      elif i==' ':
        m+=' '
  else:
    t= [[i[j:j+2] for j in range(0,len(i),2)] for i in text.split()]
    for i in t:
      for j in i:
        x = (int(j[0])-1)*5 + int(j[1])-1
        m+= alpha[x]
      m+=' '
    m = m[:-1]
  return m

