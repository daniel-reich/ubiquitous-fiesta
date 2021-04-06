
def maurice_wins(m_snails, s_snails):
  ms,mm,mf = m_snails
  ss,sm,sf = s_snails
  win = 0
  if ms > sf: win += 1
  if mm > ss: win += 1
  if mf > sm: win += 1
  if win >=2: return True
  else: return False

