
def convert_binary(string):
  ret_str = ""
  for c in string.lower():
    if c in "abcdefghijklm":
      ret_str += "0"
    else:
      ret_str += "1"
  return ret_str

