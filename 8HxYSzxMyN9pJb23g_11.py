
import textwrap as tw
def split_n_cases(t,c):
  l=len(t)
  if l/c != int(l/c) or l/c<1: return ['Error']
  return tw.TextWrapper(width=l//c).wrap(t)

