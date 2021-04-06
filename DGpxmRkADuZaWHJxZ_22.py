
def maurice_wins(m_snails, s_snails):
  return sum([int(m_snails[i] > (s_snails[-1:]+s_snails[0:2])[i]) for i in range(3)]) == 2

