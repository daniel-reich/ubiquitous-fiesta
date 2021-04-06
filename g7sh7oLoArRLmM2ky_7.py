
import re
​
def baconify(msg, mask=None):
  d = {'11110': '.', '11111': ' ', '.': '11110', ' ': '11111'}
  
  if not mask:
    msg = re.sub('\W', '', msg)
    
    get_pattern=lambda x: ''.join(['0', '1'][ch.islower()] for ch in x)
    decode=lambda x: d.get(x, chr(ord('a')+int(x, 2)))
    chunks = re.findall('\w{5}', msg)
    
    return ''.join(decode(get_pattern(chunk)) for chunk in chunks)
    
  else:
    msg = re.sub('[^\w\s.]', '', msg.lower())
    
    gen_pattern=lambda x: d.get(x, '{:05b}'.format(ord(x)-ord('a')))
    encode=lambda x: [x.upper(), x.lower(), x][int(next(code, 2))]
    code = iter(''.join(gen_pattern(ch) for ch in msg))
    
    return ''.join(encode(ch) if ch.isalpha() else ch for ch in mask)

