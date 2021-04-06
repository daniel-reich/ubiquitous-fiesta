
def maurice_wins(m_snails, s_snails):
  return all(list(map(lambda m, s: m>s, m_snails[1:], s_snails[:2])))

