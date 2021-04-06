
def maurice_wins(m_snails, s_snails):
  mscore = 0
  if m_snails[0] > s_snails[2]:
    mscore = mscore + 1
  
  if m_snails[1] > s_snails[0]:
    mscore = mscore + 1
​
  if m_snails[2] > s_snails[1]:
    mscore = mscore + 1
    
  if mscore == 2:
    return True
  else:
    return False

