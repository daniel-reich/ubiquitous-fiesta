
def truncate(txt, length):
  if not txt: return ''
  txt=txt.split()
  if len(txt[0])>length: return ''
  for i in range(2,len(txt)):
    if len(' '.join(txt[:i]))>length: return ' '.join(txt[:i-1])
  return ' '.join(txt)

