
def parse_code(txt):
  n, s, i = [x for x in txt.split('0') if len(x)]
  return {'first_name': n, 'last_name': s, 'id': i}

