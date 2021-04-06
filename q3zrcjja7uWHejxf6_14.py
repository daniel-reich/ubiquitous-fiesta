
def negative_sum(chars):
  chars = ''.join([i if i.isdigit() else ' -' if i=='-' else ' ' for i in chars]).split()
  return sum([int(i) for i in chars if int(i)<0])

