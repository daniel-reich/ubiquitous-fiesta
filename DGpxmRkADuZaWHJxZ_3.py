
def maurice_wins(m_snails, s_snails):
  return sum(m > s for m, s in zip(m_snails[1:] + m_snails[:1], s_snails)) > 1

