
def items_purchase(store, wallet):
  ans=[]
  wallet=int(''.join([j for j in wallet if j.isdigit()]))
  for i in store:
    a=int(''.join([j for j in store[i] if j.isdigit()]))
    if a<=wallet:
      ans.append(i)
  if ans: return sorted(ans)
  return "Nothing"

