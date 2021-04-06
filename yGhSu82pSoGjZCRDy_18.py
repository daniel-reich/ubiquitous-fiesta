
def seesaw(num):
  l,r,b = "left", "right", "balanced"
  if not num:
    return b
  leng = int(len(str(num))/2)
  numl,numr = [int(x) for x in str(num)[:leng]],[int(x) for x in str(num)[leng if not len(str(num)) % 2 else leng+1:]]
  return b if sum(numl) == sum(numr) else l if sum(numl) > sum(numr) else r

