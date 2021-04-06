
def widen_streets(lst, n):
  pattern = [i for i in range(len(lst[-1])) if lst[-1][i]=='#']
  wide = [''.join(i[j] if j in pattern else ' '*n for j in range(len(lst[0]))) for i in lst]
  return wide

