
def text_to_num(phone):
  convert = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
  def alpha2digit(ch):
    for i in range(2, 10):
      if ch in convert[i - 2]:
        return str(i)
    return 0
    
  def convert_char(ch):
    if ord('A') <= ord(ch) <= ord('Z'):
      return alpha2digit(ch)
    else:
      return ch
      
  return ''.join([convert_char(ch) for ch in phone])

