
d_alpha = [ 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz' ]
def club_entry(word):
  for i in d_alpha:
    if i in word.lower():
      return (d_alpha.index(i)+1)*4

