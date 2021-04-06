
def split_code(item):
  letters = ''.join(x for x in item if x.isalpha())
  digits = ''.join(x for x in item if x.isnumeric())
  return [letters,int(digits)]

