
def generate_nonconsecutive(n):
  lst = ['0', '1']
  for x in range(n-1):
    lst = [n + m for m in '01' for n in lst if '11' not in n + m]
  return ' '.join(sorted(lst))

