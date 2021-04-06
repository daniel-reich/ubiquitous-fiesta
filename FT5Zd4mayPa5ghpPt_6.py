
hex = '0123456789abcdef'
​
def color_conversion(h):
  if type(h) == str:
    if any(x not in hex+'#' for x in h):
      return "Invalid input!"
    if h[0]=='#' and len(h)==7:
      return {'r':hex_to_num(h[1:3]), 'g':hex_to_num(h[3:5]), 'b':hex_to_num(h[5:7])}
    elif h[0]!='#' and len(h)==6:
      return {'r':hex_to_num(h[0:2]), 'g':hex_to_num(h[2:4]), 'b':hex_to_num(h[4:6])}
    else:
      return "Invalid input!"
  else:
    if all(0<=h[x]<256 for x in ['r','g','b']):
      return '#{}{}{}'.format(*[num_to_hex(h[x]) for x in ['r','g','b']])
    else:
      return "Invalid input!"
    
def hex_to_num(str):
  return hex.index(str[0])*16+hex.index(str[1])
def num_to_hex(n):
  return hex[n//16]+hex[n%16]

