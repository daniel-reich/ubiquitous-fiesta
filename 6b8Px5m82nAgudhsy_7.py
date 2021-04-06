
def to_digit_arr (num):
  if num<10:
    return [num]
  return [num%10] + to_digit_arr (int(num/10))
def next_number(num):
  digs = to_digit_arr(num)
  top = digs [0]
  r = -1
  for i in range (1, len(digs)):
    if digs[i] < top:
      r = i
      break
    top = digs[i]
  if r==-1:
    return num
  res = digs [:r:-1]
  m = -1
  for i in range (r):
    if digs[r]<digs[i] and (m == -1 or digs[i]<digs[m]):
      m = i
  res += [digs[m]]
  digs[m] = digs[r]
  res += sorted(digs[:r])
  int_res = 0
  mul = 1
  for i in res[::-1]:
    int_res += i*mul
    mul*=10
  return int_res

