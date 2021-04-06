
def is_unprimeable(num):
  def is_prime(n):
    if n < 2:
      return False
    for num in range(2, n):
      if n % num == 0:
        return False
    return True
  def all_nums(num):
    
    l = list(str(num))
    
    r = range(0, 10)
    
    nums = []
    
    for n in range(0, len(l)):
      el = l
      
      for nu in r:
        tr = el[:n] + list(str(nu)) + el[n+1:]
        trs = ''
        for item in tr:
          trs += item
        tr = int(trs)
        del trs
        if tr not in nums:
          nums.append(tr)
    print(nums)
    return nums
  
  if is_prime(num) == True:
    return 'Prime Input'
  
  nums = all_nums(num)
  allprimes = []
  
  for num in nums:
    prime = is_prime(num)
    if prime == True:
      allprimes.append(num)
  
  if len(allprimes) == 0:
    return 'Unprimeable'
  else:
    return sorted(allprimes)

