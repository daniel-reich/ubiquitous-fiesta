
def is_untouchable(number):
  if number < 2: return 'Invalid Input'
  def divsum(x):
    bu = x
    i, fac = 2, []
    while i * i <= x:
      if x % i == 0:
        cnt = 0
        while x % i == 0:
          cnt += 1
          x //= i
        fac.append((i**(cnt+1)-1)//(i-1))
      i += 1
    if x >= 2: fac.append((x**2-1)/(x-1))
    from functools import reduce
    return reduce(lambda x, y: x*y, fac) - bu
  lst = [x for x in range(2, number**2+1) if divsum(x) == number]
  return lst if lst else True

