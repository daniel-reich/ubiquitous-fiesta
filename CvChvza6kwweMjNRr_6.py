
def split_code(item):
  return [''.join([i for i in item if i.isalpha()]), int(''.join([i for i in item if i.isnumeric()]))]

