
def format_num(n):
  n = str(n)[::-1]
  return ','.join([n[i:i+3] for i in range(0, len(n), 3)])[::-1]

