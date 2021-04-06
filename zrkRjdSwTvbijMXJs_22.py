
def encrypt(plncode, pad):
  res = '63719'
  for x in range(len(plncode)):
    num = int(plncode[x])- int(pad[x+5])
    res+= str(num) if num==abs(num) else str(num+10)
  return res
def decrypt(cypcode, pad):
  if not cypcode.startswith('63719') or not pad.startswith('63719'):
    return 'Error: Key IDs don\'t match.'
  res = ''
  for x in range(5,len(cypcode)):
    num = int(cypcode[x])+ int(pad[x])
    res+= str(num) if num<10 else str(num-10)
  return res

