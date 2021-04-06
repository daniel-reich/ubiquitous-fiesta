
def multiply_by_11(s, s_by_ten_rev=None, top_iter=True, sum_so_far="", pos=0, carry=0):
  if top_iter:
    s_by_ten_rev = (s + "0")[::-1]
    s = ("0" + s)[::-1]
  next_digit = int(s[pos]) + int(s_by_ten_rev[pos]) + carry
  sum_so_far += str(next_digit)[-1]
  carry = int(next_digit>9)
  if pos == len(s) - 1:
    if carry:
      sum_so_far += "1"
    return sum_so_far[::-1]
  else:
    return multiply_by_11(s, s_by_ten_rev, False, sum_so_far, pos+1, carry)

