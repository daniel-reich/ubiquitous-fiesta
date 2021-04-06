
def decrypt(s):
  h = [i for i, n in enumerate(s) if n=='#']
  conv = lambda x: chr(int(x)+96)
  is_2d = lambda i: i+1 in h or i+2 in h
  dc = [conv(s[i-2:i]) if x=='#' else conv(x)
        for i, x in enumerate(s) if x=='#' or not is_2d(i)]
  return ''.join(dc)

