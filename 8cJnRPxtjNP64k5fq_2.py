
def dance(lst, parameter):
  w_po, m_po = [], []
  for i in range(len(lst)):
    w_po.append(lst[i][0])
    m_po.append(lst[i][1])
  if parameter == 'men':
    m_po.reverse()
  else:
    w_po.reverse()
  return [[i, j] for i,j in zip(w_po, m_po)]

