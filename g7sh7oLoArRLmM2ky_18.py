
import re
​
decode = lambda s5: 'abcdefghijklmnopqrstuvwxyz..... '[int(''.join(['0' if c.isupper() else '1' for c in s5]), 2)]
encode = lambda c: bin(ord(c)-ord('a') if 'a' <= c <= 'z' else 30 if c =='.' else 31)[2:].zfill(5)
​
def baconify(msg, mask = None):
  if mask:
    cipher = ''.join(encode(c.lower()) for c in re.sub(r'[,!?:;\'\"]', '', msg))
    res, cx, mx = '', 0, 0
    while cx < len(cipher):
      if mask[mx].isalpha():
        res += mask[mx].upper() if cipher[cx] == '0' else mask[mx].lower()
        cx += 1
      else:
        res += mask[mx]
      mx += 1
    return res + mask[mx:]
  else:
    cipher = re.sub(r'[ .,!?:;\'\"]', '', msg)
    return ''.join(decode(cipher[i:i+5]) for i in range(0, len(cipher), 5) if i + 5 <= len(cipher))

