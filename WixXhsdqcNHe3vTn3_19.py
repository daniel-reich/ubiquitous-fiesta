
def how_bad(n): 
  c = "{0:b}".format(n).count('1')
  def is_pernicious(n):
    if n==2 or n==3: return ["Pernicious"]
    if n%2==0 or n<2: return []
    for i in range(3, int(n**0.5)+1, 2):   
      if n%i==0:
        return []
    return ["Pernicious"]
  def is_evil(n):
    if n%2==0: return ["Evil"]
    else: return ["Odious"]
  return sorted(is_pernicious(c)+is_evil(c))

