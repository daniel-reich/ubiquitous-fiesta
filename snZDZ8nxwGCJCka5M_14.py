
def pyramidal_string(string, _type):
  pyramid_sizes = list()
  if string == '':
    return []
  size = 1
  temp_string = string
  while True:
    if len(temp_string) > size:
      pyramid_sizes.append(size)
      temp_string = temp_string[size:]
      size += 1
    elif len(temp_string) < size:
      return 'Error!'
    else:
      pyramid_sizes.append(size)
      break
  if _type == 'REV':
    pyramid_sizes.reverse()
  pyramid = list()
  for size in pyramid_sizes:
    pyramid.append(' '.join(string[:size]))
    string = string[size:]
  return pyramid

