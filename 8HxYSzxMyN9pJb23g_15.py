
def split_n_cases(txt, cases):
  if cases > len(txt):
    return ["Error"]
  elif len(txt) % cases != 0:
    return ["Error"]
  else:
    segment_length = len(txt) / cases
    split_list = []
    x = 0
    y = int(segment_length)
    for i in range(cases):
      split_list.append(txt[x:y])
      x += int(segment_length)
      y += int(segment_length)
  return split_list

