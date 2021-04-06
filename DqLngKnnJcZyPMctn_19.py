
def stock_picker(lst):
  if sorted(lst,reverse=True)==lst:
    return -1
  lmax,lmin=max(lst),min(lst)
  limax,limin=map(lst.index,[lmax,lmin])
  if limax>limin:
    return lmax-lmin
  lmin1,lmax1=min(lst[:limax+1]),max(lst[limin:])
  return max(max([lmax-lmin1,lmax1-lmin]),stock_picker(lst[limax+1:limin]))

