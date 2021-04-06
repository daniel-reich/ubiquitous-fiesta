
def factor_sort(nums):
  def factor_length(n):
    return len(set([x for i in range(1,round(n**0.5) + 1) for x in (i,n/i) if n%i == 0]))
  
  sorted_list = sorted({k:factor_length(k) for k in nums}.items(),key = lambda x: (x[1],x[0]),reverse = True)
  return [i[0] for i in sorted_list]

