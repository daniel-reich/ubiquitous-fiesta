
def maurice_wins(m_snails, s_snails):
  did_m_won = 0
  if m_snails[0] > s_snails[2]:
    did_m_won += 1
  else:
    pass
  if m_snails[1] > s_snails[0]:
    did_m_won += 1
  else:
    pass
  if m_snails[2] > s_snails[1]:
    did_m_won += 1
  else:
    pass
​
  if did_m_won == 2 or did_m_won == 3:
    return True
  else:
    return False

