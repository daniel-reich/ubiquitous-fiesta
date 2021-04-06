
def str_to_dict(l):
  return {k:v for (k,v) in map(lambda x: x.split('='),l)}

