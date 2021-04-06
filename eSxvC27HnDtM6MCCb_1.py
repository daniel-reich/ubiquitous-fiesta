
def base_n(base, values, num):
  if len(values)!= base: return False
  ans = []
  while num:
    ans.append(str(values[num%base]))
    num//= base
  return ''.join(ans[::-1])

