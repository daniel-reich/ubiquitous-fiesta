
def maurice_wins(m_snails, s_snails):
  order = [2, 0, 1]
  s_snails = [s_snails[i] for i in order]
  return len([m for m, s in zip(m_snails, s_snails) if m > s]) >= 2

