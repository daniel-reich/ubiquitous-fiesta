
def rough_digit_length(goal):
  digit_length = lambda expon: ((10 ** (expon+1)) - (10 ** expon)) * (expon + 1) + digit_length(expon-1) if expon > 0 else 9
​
  dic = {10**(num+1):digit_length(num) for num in range(goal)}
​
  return dic
​
rdl = rough_digit_length(16)
​
def concatenation_sum(n):
​
  if n < min(rdl.keys()):
    return n
  else:
    closest = max([num for num in rdl.keys() if num <= n])
    digits = rdl[closest]
​
    digits += (n + 1 - closest) * len(str(n))
​
    return digits

