
def choose_fuse(f, c):
  f,c = (int(i.strip('V')) for i in f), float(c.strip('V'))
  return str(min(i for i in f if i>=c))+'V'

