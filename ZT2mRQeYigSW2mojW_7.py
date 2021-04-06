
def haiku(string):
  lst = string.lower().replace('.','').replace(',','').split('/')
  return sum([syl(i) for i in lst[0].split()])==5 and sum([syl(i) for i in lst[1].split()])==7 and sum([syl(i) for i in lst[2].split()])==5
  
def syl(s):
  ret = 0
  v = 'aeiou'
  ret+=sum([s.count(i) for i in v])
  if s.endswith('y'):
    ret+=1
  if any([s.endswith(i) for i in ['e','es',"e's"]]):
    ret-=1
  lst = ['ee','io','ue','ea','ai','ou','ay','ia','ie','oy']
  ret -= sum([s.count(i) for i in lst])
  if ret<1:
    ret = 1
  return ret

