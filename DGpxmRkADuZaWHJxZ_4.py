
def maurice_wins(m_snails, s_snails):
  (m1, m2, m3), (s1, s2, s3) = m_snails, s_snails
  return sum((m1 > s3, m2 > s1, m3 > s2)) == 2

