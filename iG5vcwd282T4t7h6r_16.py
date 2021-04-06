
def str_to_dict(lst):
  output = {}
  for entry in lst:
    words = entry.split('=')
    output[words[0]] = words[1]
  return output

