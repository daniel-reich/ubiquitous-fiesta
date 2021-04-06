
def validate_binary(b):
  return (len(b[:-1].replace('0','')) & 1) == int(b[-1])

