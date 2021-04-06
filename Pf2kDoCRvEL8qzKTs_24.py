
def order_people(lst, people):
  r,c =lst
  o = [0 for x in range(r*c)]
  p = [x for x in range(1,people+1)]
  o[:len(p)] = p
  asc = chunks(o,c)
  des = chunks(o[::-1],c)[::-1]
  return 'overcrowded' if r*c<people else [des[x] if x%2 else asc[x] for x in range(len(asc))]
  
def chunks(lst, n):
  return [lst[i:i + n] for i in range(0, len(lst), n)]

