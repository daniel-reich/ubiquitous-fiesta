
def vertical_txt(txt):
  strings = txt.split()
  biggest = 0
  vertical = []
  for word in strings:
    if len(word) > biggest:
      biggest = len(word)
  for i in range(1, biggest + 1):
    vertical.append([])
  for i in range(1, biggest + 1):
    for each in strings:
      if len(each) < i:
        vertical[i - 1].append(" ")
      else:
        vertical[i - 1].append(each[i - 1])
  return vertical

