
def flipping_bits(n):
  str_bin = bin(n).replace('0b','')
  arr_bin = []
  for item in str_bin:
    if item == '0':
      arr_bin.append('1')
    else:
      arr_bin.append('0')
  arr_bin_32 = ['1'] * (32-len(arr_bin)) + arr_bin
  str_bin_32 = ''.join(arr_bin_32)
  return int(str_bin_32,2)

