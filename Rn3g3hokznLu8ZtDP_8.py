
def increment_string(txt):
  if txt[-1].isalpha():
    return txt+ '1' 
  b = txt.index('0')  
  fill = len(txt) - b 
  return txt[:b] + str(int(txt[b:len(txt)])+1).zfill(fill)

