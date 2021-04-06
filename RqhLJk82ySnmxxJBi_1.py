
def power_morphic(n):
  pre = {0:'A', 1:'Ena',2:'Di',4:'Quadri',9:'Poly'}
  k = sum(str(n**i).endswith(str(n)) for i in range(2,11))
  return pre[k] + 'morphic'

