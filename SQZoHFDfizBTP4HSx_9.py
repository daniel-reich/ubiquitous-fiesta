
def missing_alphabets(txt):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  max_cnt = max([txt.count(i) for i in txt])
  return ''.join([i*(max_cnt - txt.count(i)) for i in alpha])

