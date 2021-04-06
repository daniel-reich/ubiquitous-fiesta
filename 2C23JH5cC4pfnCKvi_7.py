
def check_flush(table, hand):
  d={'S':0,'D':0,'H':0,'C':0}
  for x in table+hand:
    d[x[-1]]+=1
  for k in d:
    if d[k]>=5: return True
  return False

