
def expanded_form(n):
  a, b = str(n).split('.')
  r = [k + '0'*(len(a)-1-i) for i, k in enumerate(a) if k != '0'] + \
      [k + '/1' + '0'*(i+1) for i, k in enumerate(b) if k != '0']
  return ' + '.join(r)

