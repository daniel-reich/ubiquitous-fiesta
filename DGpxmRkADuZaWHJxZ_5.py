
def maurice_wins(m_snails, s_snails):
  s_snails.insert(0, s_snails.pop())
  return sum(m>s for m,s in zip(m_snails, s_snails)) > 1

