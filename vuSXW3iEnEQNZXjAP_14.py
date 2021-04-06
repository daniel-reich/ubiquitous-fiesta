
def create_square(length):
  return "\n".join("#"*length \
  if (i==0 or i==length-1) \
  else "#{}#".format(" "*(length-2)) \
  for i in range(length)) \
  if length is not None else ""

