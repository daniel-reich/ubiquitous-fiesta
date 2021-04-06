
def text_to_num(n):
  k = '22233344455566677778889999'
  return ''.join(k[ord(c)-65] if c.isalpha() else c for c in n)

