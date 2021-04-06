
def possibly_perfect(answers, key):
  ttl_corr, ttl_ans = 0,0
  for a,k in zip(answers, key):
    if a != "_":
      ttl_corr += a==k
      ttl_ans += 1
  return ttl_ans==ttl_corr or ttl_corr==0

