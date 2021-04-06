
def binary_conversion(txt):
  return "".join(chr(sum(int(txt[i:i+8][::-1][r])*2**r for r in range(8))) for i in range(0,len(txt),8))

