
def maurice_wins(m, s):
  m_score = 0
  s_score = 0
​
  if m[0] > s[2]:
    m_score +=1
  else:
    s_score +=1
  if m[1] > s[0]:
    m_score += 1
  else:
    s_score += 1
  if m [2] > s[1]:
    m_score += 1
  else:
    s_score += 1
  if m_score > s_score:
    return True
  else:
    return False

