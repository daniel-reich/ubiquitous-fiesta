
def color_conversion(h):
  return hex_to_dec(h) if isinstance(h,str) else dec_to_hex(h)
  
def hex_to_dec(s):
  if not all([i in '0123456789abcdef#' for i in s]) or len(s.replace('#',''))>=7:
    return 'Invalid input!'
  s = ''.join([i for i in s if i in '0123456789abcdef'])
  dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
  ret = {'r':s[0:2],'g':s[2:4],'b':s[4:6]}
  for i in ret:
    ret[i] = dic[ret[i][0]]*16+dic[ret[i][1]]
  return ret
    
def dec_to_hex(d):
  if not all([0<=d[i]<=255 for i in d]):
    return 'Invalid input!'
  lst = list('0123456789abcdef')
  ret = '#'
  for i in ['r','g','b']:
    ret+=lst[d[i]//16]+lst[d[i]%16]
  return ret

