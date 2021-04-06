
def missing_alphabets (str):
  s = sorted(set(str))
  c = lambda x: str.count(x)
  if len(s)==26:
    return ''
  else:
    l = max([c(x) for x in s])
    mis = [chr(97+i) * (l-c(chr(97+i))) for i in range(26)
            if i >= len(s) or c(s[i])<l or ord(s[i]) != 97+i]
    return ''.join(mis)

