
def dif_ciph(inpt):
  if type(inpt) == list:
    s = inpt[0]
    ans = [chr(s)]
    for i in inpt[1:]:
      s += i
      ans.append(chr(s))
    return ''.join(ans)
  else:
    ans = [ord(inpt[0])]
    ans.extend([ord(inpt[i+1]) - ord(inpt[i]) for i in range(0, len(inpt) - 1)])
    return ans

