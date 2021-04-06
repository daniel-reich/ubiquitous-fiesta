
def upload_count(d, m):
  return sum([int(i.split(' ')[0] == m) for i in d])

