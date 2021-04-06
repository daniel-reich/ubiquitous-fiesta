
def parse_code(txt):
  f_name, l_name, ID = filter(None,txt.split('0'))
  return {'first_name':f_name, 'last_name':l_name, 'id':ID}

