
def format_num(n):
  new = str(n)[::-1]
  return ','.join((new[i:i+3] for i in range(0, len(new), 3)))[::-1]

