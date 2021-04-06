
def comments_correct(txt):
  if len(txt)%2 !=0:
    return False
  chunks = []
  for n in range(0,len(txt)-2,2):
    chunks.append(txt[n:n+2])
  for i in range(len(chunks)-1):
    if chunks[i] == '/*' and chunks[i+1] != '*/':
      return False
  return True

