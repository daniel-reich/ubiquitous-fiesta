
def common_last_vowel(txt):
  v='aeiou'
  stats = [0]*5
  txt=txt.lower().split()
  for mot in txt:
    x=max([mot.rfind(j) for j in 'aeiou'])
    if x>=0: stats[v.find(mot[x])]+=1
  return v[stats.index(max(stats))]

