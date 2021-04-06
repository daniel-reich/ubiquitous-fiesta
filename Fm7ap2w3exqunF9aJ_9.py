
def count_lone_ones(n):
  n = '0' + str(n) + '0'
  return len([i for i in range(1, len(n)-1) if n[i-1] != '1' and n[i+1] != '1' and n[i] == '1'])

