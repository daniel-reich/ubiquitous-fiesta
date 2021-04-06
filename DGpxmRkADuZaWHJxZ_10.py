
def maurice_wins(m_snails, s_snails):
  rounds_win = [0, 0]
  s,m,f = 0,1,2
  rounds = [[s,f], [m,s],[f,m]]
  for i in rounds:
    if m_snails[i[0]] > s_snails[i[1]]:
      rounds_win[0] += 1
    else:
      rounds_win[1] += 1
  return rounds_win[0] > rounds_win[1]

