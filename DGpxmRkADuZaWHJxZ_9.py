
def maurice_wins(m_snails, s_snails):
  m = m_snails 
  s = s_snails 
  if (m[0]>s[2] and m[1]>s[0]) or (m[1]>s[0] and m[2]>s[1]) or (m[0]>s[2]and m[2]>s[1]):
    return True
  return False

