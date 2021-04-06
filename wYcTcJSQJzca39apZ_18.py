
def truncate(txt, length):
  if len(txt) < length: return txt
  if txt.find(' ') + 1 > length: return ''  
  elif txt[length] == ' ': return txt[:length]
  else: return txt[:txt.rfind(' ',0,length)]

