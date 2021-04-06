
def how_mega_is_it(n):
  num = '1' + (len(str(n)[1:].split('.')[0]) * '0')
  if n < 0:
    num = num[:-1]
  if 0 <= n < 100:
    return "not a mega milestone"
  else:
    mega = num.count('0') - 1
    return '{} milestone'.format(' '.join(mega * "MEGA".split(' ')))

