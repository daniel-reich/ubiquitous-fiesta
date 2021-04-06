
def parse_code(txt):
  a = txt.replace('0',' ')
  b = ' '.join(a.split())
  c = b.split(' ')
  d = ['first_name','last_name','id']
  return dict(zip(d,c))

