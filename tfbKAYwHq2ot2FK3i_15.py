
def non_repeats(radix):
  num_po = 1
  c = 0
  ans = 0 
  for len_num in range (1,radix+1 ):
    for i in range (len_num):
      num_po *= radix-c 
      if i == 0:
        num_po  -= num_po/(radix-c)
      c+= 1 
   
    c      = 0 
    ans   += num_po   
    num_po = 1     
  return ans

