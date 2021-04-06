
def maurice_wins(m_snails, s_snails):
  s1=m_snails[0]
  m1=m_snails[1]
  f1=m_snails[2]
  s2=s_snails[0]
  m2=s_snails[1]
  f2=s_snails[2]
  
  return (s1>f2 and m1>s2) or (s1>f2 and f1>m2) or (m1>s2 and f1>m2)

