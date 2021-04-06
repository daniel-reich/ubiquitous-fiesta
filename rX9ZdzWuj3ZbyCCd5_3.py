
def multiply_by_11(s, carry = 0):
  if not s and not carry:
    return ''
  a = s[-1] if s else 0
  carry, nex = divmod(int(a)+carry,10)
  carry+= int(a)
  return multiply_by_11(s[:-1], carry) + str(nex)

