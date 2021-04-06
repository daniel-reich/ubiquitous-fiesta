
def sock_pairs(socks):
  
  l8rs = list(set(socks)) 
  pairs = 0
  
  for l8r in l8rs:
    c = socks.count(l8r)
    pairs += int(c / 2)
  
  return pairs

