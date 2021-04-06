
def camel_to_snake(s):
  return "".join("_" + ch.lower() if ch.isupper() else ch.lower() for i, ch in enumerate(s))

