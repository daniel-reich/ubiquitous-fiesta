
def constraint(txt):
  lst = list(range(97,123))
  txt2 = ''.join(i.lower() for i in txt if i not in ' ,.!?')
  n = 0
  for i in txt2:
    if ord(i) in lst: lst.remove(ord(i))
    else: n+=1
  if not lst: return 'Pangram'
  elif n==0: return "Heterogram"
  elif all(i[0].lower()==txt[0].lower() for i in txt.split(' ')): return "Tautogram"
  elif any(all(k in j for j in txt.lower().split(' ')) for k in txt.lower().split(' ')[0]): return "Transgram"
  else: return "Sentence"

