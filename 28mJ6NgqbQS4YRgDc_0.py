
def can_pay_cost(ma, co):
  n = ''.join(d for d in co if d.isdigit())
  return all(ma.count(T)>=co.count(T) for T in 'WUBRGC') and \
              len(ma)>=len(co) - len(n) + (int(n) if n else 0)

