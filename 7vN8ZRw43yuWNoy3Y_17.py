
def parse_code(txt):
  names = [word for word in txt.split('0') if word != '']
  return {'first_name':names[0], 'last_name':names[1], 'id': names[2]}

