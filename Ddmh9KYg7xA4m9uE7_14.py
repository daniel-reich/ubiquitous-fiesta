
def convert_binary(string):
  return "".join([str(1) if i.lower() >= "n" else str(0) for i in string])

