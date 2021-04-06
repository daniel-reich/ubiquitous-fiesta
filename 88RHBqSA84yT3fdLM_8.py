
def inator_inator(inv):
  return '{}{} {}000'.format(inv,'-inator' if inv[-1].lower() in ('a','e','i','o','u') else 'inator',len(inv))

