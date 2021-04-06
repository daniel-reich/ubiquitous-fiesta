
def mod(base, key):
    fact, loop = [1], 0
    for i in range(1, key+1):fact+=[fact[-1]*i]
    for i in range(base):
      if i<key:loop+=fact[i]
      elif i!=key:
        r = (fact[-1]*i%fact[-1])%fact[-1]
        if r:fact+=[r]
        loop+=fact[-1]
    return loop % fact[key]

