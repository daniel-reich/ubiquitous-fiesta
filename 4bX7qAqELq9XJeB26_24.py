
def to_camel_case(txt):
  txt_mod = txt.replace('-', '_').split('_')
  if len(txt_mod) <= 1:
    return ''.join(txt_mod)
  return ''.join(txt_mod[0]) + ''.join([i.capitalize() for i in txt_mod[1:]])

