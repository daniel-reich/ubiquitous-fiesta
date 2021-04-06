
def esthetic(num):
  return [i for i in range(2,11) if pair_dif(dec_to_base(num,i))] or "Anti-Esthetic"
  
def dec_to_base(num,base): #base <= 10
    base_num = ''
    while num>0:
        base_num += str(num%base)
        num //= base
    return base_num[::-1]
  
def pair_dif(num):
  return all([1==abs(int(a)-int(b)) for a,b in zip(str(num)[:-1],str(num)[1:])])

