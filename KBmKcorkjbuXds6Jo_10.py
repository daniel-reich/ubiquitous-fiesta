
def chocolates_parcel(n_s, n_b, order):
  a,b=divmod(order, 5)
  if n_s==1:
    return -1
  else:
    if a<=n_b:
      if b//2<=n_s:
        if b%2==0:
          return b//2
        else:
          if (b+5)//2<=n_s:
            return (b+5)//2
          else:
            return -1
      else:
        return -1
    else:
      r=(a-n_b)*5+b
      if r//2<n_s:
        if r%2==0:
          return r//2
        else:
          if (r+5)//2<=n_s:
            return (r+5)//2
          else:
            return -1
      else:
        return -1

