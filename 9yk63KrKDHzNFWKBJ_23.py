
def is_it_inside(d1,ch,pa):
  def get_key(val):
   if val == pa:
    return True
   for k1,v1 in d1.items():
     if val in v1:
       if k1==pa:
        return True
       else:
        while k1!=pa:
          return get_key(k1)
   return False
  return get_key(ch)

