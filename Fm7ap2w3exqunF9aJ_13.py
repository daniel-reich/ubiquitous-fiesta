
def count_lone_ones(n):
  return ''.join('1' if d=='1' else '0' for d in str(n)).split('0').count('1')

