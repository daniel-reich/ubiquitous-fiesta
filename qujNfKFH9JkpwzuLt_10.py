
def first_index(hex_val, needle):
  bytes_arr = bytearray.fromhex(hex_val)
  decoded = bytes_arr.decode(errors='replace')
  return decoded.find(needle)

