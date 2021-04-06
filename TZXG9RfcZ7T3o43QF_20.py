
from itertools import groupby
def same_length(txt):
  grp = [(k,sum(1 for _ in g)) for k,g in groupby(txt)]
  ones = [grp[i][1] for i in range(len(grp)) if grp[i][0]=='1']
  zeros = [grp[i][1] for i in range(len(grp)) if grp[i][0]=='0']
  return ones == zeros

