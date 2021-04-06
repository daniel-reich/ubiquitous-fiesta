
def maurice_wins(m_snails, s_snails):
  m_count = 0
  win_list = [(m_snails[0], s_snails[2]), (m_snails[1], s_snails[0]), (m_snails[2], s_snails[1])]
  for i in range(0, len(win_list)):
    if win_list[i][0] > win_list[i][1]:
      m_count += 1
  print(m_count)
  return m_count >= 2

