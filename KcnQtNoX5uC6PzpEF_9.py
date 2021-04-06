
def check_sum(lst, n):
  return bool([i for i in lst if (n-i) in lst and n!=i*2])

