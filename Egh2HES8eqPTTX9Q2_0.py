
def rolling_cipher(txt, n):
  from string import ascii_lowercase as al
  return ''.join([al[(al.find(c)+n)%26] for c in list(txt)])

