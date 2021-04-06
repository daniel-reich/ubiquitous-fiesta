
def base_conv(n,b):
  if type(n) == int:
    ans = ""
    while n:
      ans = chr(n%b + 97) + ans
      n = n//b
    return ans
  else:
    if any(ord(l)-97 >= b or ord(l)-97 < 0 for l in n):
      return n + " is not a base " + str(b) + " number."
    return sum((ord(n[::-1][i])-97)*b**i for i in range(len(n)))

