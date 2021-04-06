
def get_drink_ID(f, v):
  return ''.join(i[:3].upper() for i in f.split(' ')) + v.strip('ml')

