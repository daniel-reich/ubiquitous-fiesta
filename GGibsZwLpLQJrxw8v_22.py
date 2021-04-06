
def get_lucky_number(size, nth):
  res = [x for x in range(1,size+1) if x&1]
  i = 1
  elim = res[i]
  while elim < len(res):
    res = [n for ind,n in enumerate(res) if (ind+1)%elim]
    i += 1
    elim = res[i]
  return res[nth-1]

