
def wave(txt):
  return [txt[:index]+txt[index].upper()+txt[index+1:] for index, char in enumerate(txt) if index != len(txt) and char != ' ']

