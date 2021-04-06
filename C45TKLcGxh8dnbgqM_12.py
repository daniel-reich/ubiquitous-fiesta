
def caesar_cipher(s, k):
  nstr = ''
  print(k, s)
  for ch in s:
    asc = ord(ch)
    print(ch, asc)
    #lowercase
    if 122 >= asc >= 97:
      nasc = asc + k
      while nasc > 122:
        nasc = nasc - 26
    #uppercase
    elif 90 >= asc >= 65:
      nasc = asc + k
      while nasc > 90:
        nasc = nasc - 26
    else:
      nasc = asc
    #change character
    nstr = nstr + (chr(nasc))
  return nstr

