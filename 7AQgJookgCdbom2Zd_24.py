
def pig_latin(txt):
  st2=""
  res=""
  for i in txt:
      if not i in ['.','!']:
          st2+=i
  lst=st2.split(" ")
  ll=[]
  for i in lst:
      if not i[0].lower() in ['a','e','i','o','u']:
          ll.append(i[1:]+i[0].lower()+'ay')
      else:
          ll.append(i+'way')
  st3=" ".join(ll)
  for i in range(len(st3)):
      if i==0:
          res+=st3[i].upper()
      else:
          res+=st3[i]
  if len(lst)>1:
    return res+'.'
  else:
    return res+'!'

