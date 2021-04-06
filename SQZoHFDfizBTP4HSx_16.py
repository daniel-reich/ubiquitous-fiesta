
def missing_alphabets(txt):
  alp = "abcdefghijklmnopqrstuvwxyz"
  counts = []
  c = []
  
  for i in txt:
    counts.append(txt.count(i))
  
  maks = max(counts)
  sortedalp = sorted(alp*maks)
  
  for i in txt:
    if i in sortedalp:
      sortedalp.remove(i)
  
  return "".join(sortedalp)

