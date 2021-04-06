
import re
def baconify(msg, *mask):
  if not mask:
    msg = ''.join('1' if ch.islower() else '0' for ch in re.findall('[a-zA-Z]',msg))
    msg = msg[:5*(len(msg)//5)]
    lst = [int('0b' + msg[i:i+5],2) for i in range(0,len(msg),5)]
    res = ''.join([chr(i+97) if i < 30 else chr(46) if i == 30 else chr(32) for i in lst])
    return res
  else:
    mask = list(mask[0])
    msg = ''.join('{0:05b}'.format(ord(ch)-97) if ch.isalpha() else '11111' if ch == ' ' else '11110' if ch == '.' else '' for ch in msg.lower())
    
    i, j = 0, 0
    while i < len(mask) and j < len(msg):
      if mask[i].isalpha():
        if msg[j] == '1':
          mask[i] = mask[i].lower()
        else:
          mask[i] = mask[i].upper()
        i += 1
        j += 1
      else:
        i += 1
    return ''.join(mask)

