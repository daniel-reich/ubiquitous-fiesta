
#First capitalize txt 
#Second replace first capitalize letter with lowwer one
#Third check if there is '_'  and remove it 
#Forth join the sentence together  
#~~~~~~~~~~~~~~~~~~~~~
def camelCasing(txt):
  txt=txt.title()
  txt=list(txt)
  txt.insert(0,txt[0].lower())
  txt.remove(txt[1])
  for i in txt:
    if i=='_':
      txt.remove('_')
  return(''.join(txt).replace(' ',''))

