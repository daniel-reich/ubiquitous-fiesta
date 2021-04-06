
def binary_conversion(txt):
  if( txt == "" ):
    return txt
  return ''.join(chr(int(txt[i*8:i*8+8],2)) for i in range(len(txt)//8))

