
def gcdm(num,dem):
  while dem:
    num, dem = dem, num%dem
  return num
def mixed_number(frac):
    neg=''
    f=frac.split('/')
    num,dem=int(f[0]),int(f[1])
    if num<0:
        num=-num
        neg='-'
    gcd = gcdm(num,dem)
    num,dem = num/gcd, dem/gcd
    if num//dem!=0 and num%dem!=0:
        return neg+str(int(num//dem))+' '+str(int(num%dem))+'/'+str(int(dem))
    if num%dem==0:
        return neg+str(int(num//dem))
    return neg+str(int(num%dem))+'/'+str(int(dem))

