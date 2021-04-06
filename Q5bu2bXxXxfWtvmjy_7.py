
def missing_letter(txt):
  for i in range(1,len(txt)):
    if ord(txt[i])-ord(txt[i-1])>1: return chr(ord(txt[i])-1)
  return 'No Missing Letter'

