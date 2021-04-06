
def truncate(txt, length):
  if length >= len(txt): return txt
  spaces = [k for k, v in enumerate(txt) if v == " "] + [len(txt)]
  if length < spaces[0]: return ""
  for i in range(len(spaces)):
    if spaces[i] > length: return txt[:spaces[i-1]]

