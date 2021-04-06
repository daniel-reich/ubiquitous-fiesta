
def split_code(item):
  N = sum([x.isalpha() for x in item])
  return [item[:N], int(item[N:])]

