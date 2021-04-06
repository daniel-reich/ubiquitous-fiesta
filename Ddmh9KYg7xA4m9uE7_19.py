
def convert_binary(string):
  zeros = [chr(i) for i in range(97,110)]
  out = ""
  for i in string.lower():
    if i in zeros:
      out += "0"
    else:
      out += "1"
  return out

