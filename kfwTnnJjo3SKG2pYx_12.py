
def replace_nums(s):
  return __import__('re').sub('\d+', lambda x: bin(int(x.group(0)))[2:], s)

