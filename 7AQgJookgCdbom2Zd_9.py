
def pig_latin(txt):
  v='aeiou'
  p='.!?,'
  txt=txt.split()
  for i in range(len(txt)):
    if txt[i][0].lower() in v: 
      if txt[i][-1] not in p: txt[i]=txt[i]+'way'
      else: txt[i]=txt[i][:-1]+'way'+txt[i][-1]
    else: 
      if txt[i][-1] not in p: txt[i]=txt[i][1:]+txt[i][0].lower()+'ay'
      else: txt[i]=txt[i][1:-1]+txt[i][0].lower()+'ay'+txt[i][-1]
  txt[0]=txt[0][0].upper()+txt[0][1:]
  return ' '.join(txt)

