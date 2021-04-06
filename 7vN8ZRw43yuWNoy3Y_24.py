
def parse_code(txt):
  name, last, id  = [i for i in txt.split('0') if i]
  return {'first_name': name, 'last_name': last, 'id': id}

