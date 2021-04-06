
def is_autobiographical(n):
  st = str(n)
  return all(int(st[i]) == st.count(str(i)) for i in range(len(st)))

