
def maurice_wins(m_snails, s_snails):
  sum = 0
  if m_snails[0]>s_snails[2]:
    sum+=1
  if m_snails[1]>s_snails[0]:
    sum+=1
  if m_snails[2]>s_snails[1]:
    sum+=1
  return sum>1

