
def mod_inv(n, m):
  n_n, n_m, m_n, m_m = 1,0, 0,1
  while n>0:
    n, m, n_n, n_m, m_n, m_m = m % n, n, m_n - (m//n)*n_n, m_m - (m//n)*n_m, n_n, n_m
  if m != 1:
    return False
  return m_n

