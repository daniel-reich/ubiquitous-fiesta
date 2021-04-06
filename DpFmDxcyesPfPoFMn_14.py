
_isbn10 = "987654321"
_isbn13 = "1313131313131"
​
def isbn13(txt):
  if len(txt) == 13:
    return 'Valid' if m_s(_isbn13, txt) % 10 == 0 else 'Invalid'
  elif len(txt) == 10:
    suma = int(txt[0]) * 10
    suma += m_s(_isbn10, txt[1:])
    if suma % 11 == 0:
      for j in range(0, 10):
        if isbn13('978' + txt[0:len(txt) - 1] + str(j)) == 'Valid':
          return '978' + txt[0:len(txt) - 1] + str(j)
    else:
      return 'Invalid'
  return 'Invalid'
​
def m_s(s1, s2):
  cum = 0
  for i in range(0, len(s2)):
    if s2[i].upper() == 'X':
      cum += int(s1[i]) * 10
    else:
      cum += (int(s1[i]) * int(s2[i]))
  return cum

