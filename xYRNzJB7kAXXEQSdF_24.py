
def wiggle_string(s):
  output = []
  offset = 0
  while offset < len(s)+1:
    output.append((' '*offset+s))
    offset += 1
  offset -= 2
  while offset > -1:
    output.append((' '*offset+s))
    offset -= 1
  return output

