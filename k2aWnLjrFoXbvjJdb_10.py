
ORD_A = ord('A')
​
def encode_character(ptch, kwch):
  c, r = ord(ptch) - ORD_A, ord(kwch) - ORD_A
  return chr(((r + c) % 26) + ORD_A)
​
def decode_character(ench, kwch):
  e, r = ord(ench) - ORD_A, ord(kwch) - ORD_A
  return chr(((e - r) % 26) + ORD_A)
​
def vigenere(text, keyword):
  txt = ''.join(map(str.upper, [c for c in text if c.isalpha()]))
  func = decode_character if txt == text else encode_character
  keyword = keyword.upper() * (1 + len(txt) // len(keyword))
  return ''.join([func(txt[i], keyword[i]) for i in range(len(txt))])

