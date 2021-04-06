
def is_undulating(n):
  if n<100: return False
  return all(str(n)[i]==str(n)[0] for i in range(0,len(str(n)),2)) \
    and all(str(n)[i]==str(n)[1] for i in range(1,len(str(n)),2))

