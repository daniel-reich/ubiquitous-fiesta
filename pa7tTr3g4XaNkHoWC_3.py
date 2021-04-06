
def pig_latin_sentence(s):
  l=[]
  for x in s.split():
    if x[0]in'aeiou':w=x+'way'
    else:
      w=''
      for i,y in enumerate(x):
        if y not in'aeiou':w+=y
        else:w=x[i:]+w+'ay';break
    l.append(w)
  return' '.join(l)

