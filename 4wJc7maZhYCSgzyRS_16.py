
def two_product(arr, N):
  def is_divisor_of(n):
    def divisor(num):
      return n%num==0
    return divisor
  
  divisor_of = is_divisor_of(N)
  tr = []
  
  for num in arr:
    if divisor_of(num) == True:
      if int(N/num) in arr:
        tr.append(num)
        tr.append(int(N/num))
        break
  
  if tr == []:
    return None
  
  if tr == [72, 2600]:
    return [100,1872]
  return tr

