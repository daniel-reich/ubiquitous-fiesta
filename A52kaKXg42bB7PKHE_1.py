
def num_then_char(l):
  n=sorted(sum(l,[]),key=lambda e:((e,100)[type(e)==str],e))
  for x in[len(y)for y in l]:
    n.append(n[:x])
    del n[:x]
  return n

