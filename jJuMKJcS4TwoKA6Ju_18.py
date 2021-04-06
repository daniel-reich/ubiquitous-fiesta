
def dial(txt):
  meh = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
  dic = {l:str(i+2) for i,ch in enumerate(meh) for l in ch}
  
  return ''.join(dic[l] if l in dic else l for l in txt.lower())

