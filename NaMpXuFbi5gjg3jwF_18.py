
def sock_pairs(socks):
  lst = set(list(socks))
  pairs = 0
​
  for item in lst:
    pairs += socks.count(item)//2
​
  return pairs

