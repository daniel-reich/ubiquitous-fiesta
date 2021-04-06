
def increment_string(txt):
  if txt[-1].isdigit():
    integer = txt[-1]
    i = 2
    while txt[-i].isdigit():
      integer = txt[-i] + integer
      i += 1
    i -= 1
    orig_len = len(integer)
    num = int(integer) + 1
    zeros = ""
    if len(str(num)) < orig_len:
      diff = orig_len - len(str(num))
      zeros = '0' * diff
    return txt[:-i] + zeros + str(num)
  else:
    return(txt+'1')

