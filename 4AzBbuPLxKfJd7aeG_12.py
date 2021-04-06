
def encrypt(key, message):
  l=['#']
  for i in range(0,len(key),2):
    l.append(key[i])
    l.append(key[i+1])
    l.append('#')
    
  en=''
  for i in message:
    j=str.lower(i)
    if(j not in l):
      en+=i
    else:
      index=l.index(i)
      if(l[index-1]=='#'):
        en+=l[index+1]
      else:
        en+=l[index-1]
  return en

