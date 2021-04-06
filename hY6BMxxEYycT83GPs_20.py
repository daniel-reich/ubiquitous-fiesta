
def multiply_by_11(n):
  n = '0'+n[::-1]+'0'
  fin = ''
  carry = False
  for a,b in zip(n,n[1:]):
    a,b = int(a),int(b)
    cur = a+b
    if carry:
      cur+=1
      carry = False
    fin+=str(cur%10)
    if cur>=10:
      carry = True
  return '1'+fin[::-1] if carry else fin[::-1]

