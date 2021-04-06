
def high_low(txt):
  num_list = [int(ch) for ch in txt.split(' ')]
  return ' '.join((str(max(num_list)), str(min(num_list))))

