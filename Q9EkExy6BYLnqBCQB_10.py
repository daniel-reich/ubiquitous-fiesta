
def wrap_around(string, offset):
  if abs(offset) < len(string):
          return string[offset:]+string[:offset]
  else:
      a = offset%len(string)
      return string[a:]+string[:a]

