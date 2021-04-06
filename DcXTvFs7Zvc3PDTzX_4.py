
def validate_binary(b):
  return b.count("1")%2==0 and b.count("0")%2==0 and b.count("1")%2==b.count("0")%2

