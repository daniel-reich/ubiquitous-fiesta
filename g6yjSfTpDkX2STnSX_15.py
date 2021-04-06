
def convert_to_hex(txt):
  output=""
  for x in txt:
    output+=hex(ord(x))[2::] + " "
  return output[:-1]

