
def maurice_wins(m_snails, s_snails):
  wins=0
  if m_snails[1]>s_snails[0]: wins+=1
  if m_snails[2]>s_snails[1]: wins+=1
  return wins==2

